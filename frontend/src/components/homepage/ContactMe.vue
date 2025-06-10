<script setup>
import { ref, computed, onMounted } from 'vue'
import { useLanguage } from '../../composables/useLanguage'
import FadeContent from '../effects/fadeContent/FadeContent.vue'
import ScrollReveal from '../effects/scrollReveal/ScrollReveal.vue'
import RevealLink from '../effects/flipLink/RevealLink.vue'
import ShinyBorder from '../effects/shinyBorder/ShinyBorder.vue'
import EncryptButton from '../effects/encryptButton/EncryptButton.vue'
import Aurora from '../effects/backgroundVideo/Aurora.vue'

const { lang, getText } = useLanguage()

// --- Social links (left panel) ---
const socialItems = [
  { key: 'linkedin', url: 'https://linkedin.com/in/valeri-levinson', display: 'my linkedin' },
  { key: 'email',    url: 'mailto:levinsonvaleri@gmail.com', display: 'levinsonvaleri@gmail.com' },
  { key: 'phone',    url: 'tel:+9720552251273', display: '+972-055-2251273' },
  { key: 'cv',       url: '/valerilevinson_CV.pdf', display: 'Download CV', download: true },
]

// --- Form & reCAPTCHA & Alert state (right panel) ---
const buttonDisabled      = ref(false)
const formData            = ref({ name: '', email: '', phone: '', message: '' })
const showAlert           = ref(false)
const alertType           = ref('')       // 'success' | 'error'
const alertMessage        = ref('')
const typingEffectRunning = ref(false)

// Load reCAPTCHA on mount
const loadRecaptchaScript = () =>
  new Promise((resolve, reject) => {
    if (document.getElementById('recaptcha-script')) return resolve()
    const s = document.createElement('script')
    s.id = 'recaptcha-script'
    s.src = 'https://www.google.com/recaptcha/api.js?render=6Lfz4qgqAAAAAJj4s5Vd7bHfsqIrhc65dsAHxOQc'
    s.onload  = resolve
    s.onerror = () => reject(new Error('reCAPTCHA load failed'))
    document.head.appendChild(s)
  })
onMounted(loadRecaptchaScript)

// Typing‐effect for alert
function typingEffect() {
  if (typingEffectRunning.value) return
  typingEffectRunning.value = true
  const full = alertMessage.value
  alertMessage.value = ''
  let i = 0
  const speed = 50
  function type() {
    if (i < full.length) {
      alertMessage.value += full[i++]
      setTimeout(type, speed)
    } else {
      typingEffectRunning.value = false
      buttonDisabled.value = false
    }
  }
  type()
}

// Send message
async function sendMessage() {
  buttonDisabled.value = true
  showAlert.value    = false
  alertMessage.value = ''

  try {
    await loadRecaptchaScript()
    const token = await window.grecaptcha.execute('6Lfz4qgqAAAAAJj4s5Vd7bHfsqIrhc65dsAHxOQc', { action: 'submit' })
    const res   = await fetch('https://portfolio.valerilevinson.com/api/message', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ ...formData.value, recaptchaToken: token })
    })
    if (!res.ok) throw new Error('Network error')
    alertType.value    = 'success'
    alertMessage.value = getText('contact.alerts.success')
  } catch (e) {
    console.error(e)
    alertType.value    = 'error'
    alertMessage.value = getText('contact.alerts.error')
  }

  showAlert.value = true
  typingEffect()
}

// Close Alert
function handleClose() {
  showAlert.value = false
}
</script>

<template>
<section class="contact-me relative w-full bg-sections-contact_me rounded-md h-screen overflow-hidden border border-red-100">
  <div   class="h-screen flex justify-around items-center gap-6 mx-auto  px-4 "
  >
    <!-- LEFT PANEL: Social Links -->
    <FadeContent
      class-name="social-panel w-1/3"
      :blur="true"
      :duration="800"
      easing="ease-out"
      :initial-opacity="0"
      :y-offset="20"
    >
      <!-- <h3 class="uppercase underline mb-4">
        {{ getText('contact.social') }}
      </h3> -->
      <RevealLink/>
    </FadeContent>

    <!-- RIGHT PANEL: Contact Form -->
    <FadeContent
      class-name="form-panel w-1/3"
      :blur="true"
      :duration="800"
      easing="ease-out"
      :initial-opacity="0"
      :y-offset="20"
    >
      <p class="uppercase mb-4 text-6xl font-black whitespace-nowrap">
        {{ getText('contact.messageTitle') }}
      </p>
      <form @submit.prevent="sendMessage" class="max-w-[40rem]">

        <!-- Name -->
        <label class="block text-sm">
          {{ getText('contact.form.name') }}
        </label>
        <div class="trace-input">
          <input
            v-model="formData.name"
            type="text"
            required
            :placeholder="getText('contact.form.placeholder.name')"
            class=""
          />
          <span class="trace bottom"></span>
          <span class="trace right"></span>
          <span class="trace top"></span>
          <span class="trace left"></span>
        </div>

        <!-- Email -->
        <label class="text-sm">
          {{ getText('contact.form.email') }}
        </label>
        <div class="relative trace-input">
          <input
            v-model="formData.email"
            type="email"
            required
            :placeholder="getText('contact.form.placeholder.email')"
            class="w-full bg-opacity-20"
          />
          <span class="trace bottom"></span>
          <span class="trace right"></span>
          <span class="trace top"></span>
          <span class="trace left"></span>
        </div>

        <!-- Phone -->
        <label class=" text-sm">
          {{ getText('contact.form.phone') }}
        </label>
        <div class="relative trace-input">
          <input
            v-model="formData.phone"
            type="tel"
            :placeholder="getText('contact.form.placeholder.phone')"
            class="w-full"
          />
          <span class="trace bottom"></span>
          <span class="trace right"></span>
          <span class="trace top"></span>
          <span class="trace left"></span>
        </div>

        <!-- Message -->
        <label class="text-sm text-primary-300">
          {{ getText('contact.form.message') }}
        </label>
        <div class="relative trace-input">
          <textarea
            v-model="formData.message"
            rows="4"
            required
            :placeholder="getText('contact.form.placeholder.message')"
            class=""
          ></textarea>
          <span class="trace bottom"></span>
          <span class="trace right"></span>
          <span class="trace top"></span>
          <span class="trace left"></span>
        </div>

        <!-- Submit Button -->
        <EncryptButton
          type="submit"
          :disabled="buttonDisabled"
          :targetText="getText('contact.form.button')"
          
        >
          <!-- <span
            v-if="buttonDisabled"
            class="w-5 h-5 border-2 border-current border-t-transparent rounded-full animate-spin"
          />
          {{ getText('contact.form.button') }} -->
      </EncryptButton>
      </form>
    </FadeContent>
  </div>
    <!-- ALERT OVERLAY -->
    <div
      v-if="showAlert"
      @click="handleClose"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-30 z-50"
    >
      <div
        @click.stop
        :class="[
          'p-4 rounded-md text-center',
          alertType === 'success'
            ? 'bg-messages-success'
            : 'bg-messages-error'
        ]"
      >
        <p class="font-pixelify text-primary-300">{{ alertMessage }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.social-panel { 

 }
.form-panel   { /* right panel overrides if needed */ }


.trace-input {
  position: relative;
  margin-bottom: 1rem;
}

/* common input/textarea styles */
.trace-input input,
.trace-input textarea {
  width: 100%;
  color: #f2f2f2;
  font-size: 1rem;
  font-family: inherit;
  background-color: hsla(235, 16%, 54%, 0.207);
  padding: 0.75em 0.5em;
  border: 1px solid transparent;
  transition: background-color 0.3s ease-in-out;
}

/* remove default focus */
.trace-input input:focus,
.trace-input textarea:focus {
  outline: none;
}

/* placeholder color */
.trace-input input::placeholder,
.trace-input textarea::placeholder {
  color: hsla(0, 0%, 100%, 0.6);
}

/* the four animated spans */
.trace {
  position: absolute;
  background-color: #fc2f70;
  transition: transform 0.1s ease;
}

.bottom,
.top {
  height: 1px;
  left: 0;
  right: 0;
  transform: scaleX(0);
}

.left,
.right {
  width: 1px;
  top: 0;
  bottom: 0;
  transform: scaleY(0);
}

.bottom {
  bottom: 0;
  transform-origin: bottom right;
}
.trace-input input:focus ~ .bottom,
.trace-input textarea:focus ~ .bottom {
  transform-origin: bottom left;
  transform: scaleX(1);
}

.right {
  right: 0;
  transform-origin: top right;
  transition-delay: 0.05s;
}
.trace-input input:focus ~ .right,
.trace-input textarea:focus ~ .right {
  transform-origin: bottom right;
  transform: scaleY(1);
}

.top {
  top: 0;
  transform-origin: top left;
  transition-delay: 0.15s;
}
.trace-input input:focus ~ .top,
.trace-input textarea:focus ~ .top {
  transform-origin: top right;
  transform: scaleX(1);
}

.left {
  left: 0;
  transform-origin: bottom left;
  transition-delay: 0.25s;
}
.trace-input input:focus ~ .left,
.trace-input textarea:focus ~ .left {
  transform-origin: top left;
  transform: scaleY(1);
}

</style>
