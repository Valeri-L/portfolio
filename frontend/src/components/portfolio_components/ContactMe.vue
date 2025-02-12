<script setup>
import { ref, computed,onMounted } from 'vue';



// Button disabled state
const buttonDisabled = ref(false)


const loadRecaptchaScript = () => {
  return new Promise((resolve, reject) => {
    if (document.getElementById('recaptcha-script')) {
      resolve();
      return;
    }

    const recaptchaScript = document.createElement('script');
    recaptchaScript.id = 'recaptcha-script';
    recaptchaScript.src = 'https://www.google.com/recaptcha/api.js?render=6Lfz4qgqAAAAAJj4s5Vd7bHfsqIrhc65dsAHxOQc';
    recaptchaScript.onload = resolve;
    recaptchaScript.onerror = () => reject(new Error('Failed to load reCAPTCHA script.'));
    document.head.appendChild(recaptchaScript);
  });
};


const initializeRecaptcha = async () => {
  await loadRecaptchaScript(); // Ensure the script is loaded
  return new Promise((resolve) => {
    if (window.grecaptcha) {
      window.grecaptcha.ready(() => resolve());
    } else {
      reject(new Error('grecaptcha is not defined.'));
    }
  });
};

onMounted(() => {
  loadRecaptchaScript();
});


// Form data
const formData = ref({
  name: '',
  email: '',
  phone: '',
  message: ''
});

// Reactive properties for alert
const showAlert = ref(false);
const alertType = ref('');
const alertMessage = ref('');
const typingEffectRunning = ref(false);

// Send Message function
const sendMessage = async () => {
  buttonDisabled.value = true
  resetState(); // Reset previous state

  // Create an AbortController for timeout
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 5000); // Timeout after 3 seconds

  try {
    // Request reCAPTCHA token
    const token = await grecaptcha.execute('6Lfz4qgqAAAAAJj4s5Vd7bHfsqIrhc65dsAHxOQc', { action: 'submit' });

    if (!token) {
      throw new Error('Failed to get reCAPTCHA token.');
    }

    // 'https://portfolio.valerilevinson.com/api/message'
    //  'http://127.0.0.1:8000/api/message'
    // Include the token in the payload
    const response = await fetch('https://portfolio.valerilevinson.com/api/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        ...formData.value,
        recaptchaToken: token, // Add reCAPTCHA token to the payload
      }),
      signal: controller.signal, // Attach the AbortController signal
    });

    clearTimeout(timeoutId); // Clear the timeout if the request succeeds


    if (!response.ok) {
      throw new Error('Failed to send message.');
    }

    const result = await response.json();
    alertMessage.value = "Message sent successfully!";
    alertType.value = 'success';
  } catch (error) {
    clearTimeout(timeoutId); // Ensure timeout is cleared in case of any error

    if (error.name === 'AbortError') {
      console.error("Request timed out:", error);
      alertMessage.value = "server is unreachable. Please try again later.";
    } else {
      console.error("Error in sendMessage:", error);
      alertMessage.value = "An error occurred. Please try again.";
    }
    alertType.value = 'error';
  }

  // Invoke typing effect if needed
  if (!typingEffectRunning.value && alertMessage.value) {
    typingEffect();
    //the whole point here is to close the typing effect no matter what at the end.
    setTimeout(()=>{
      resetState()
      if(alertType.value === 'success'){
        buttonDisabled.value = false
        location.reload()
      }
      if(alertType.value === 'error'){
        buttonDisabled.value = false
      }
    },4000)
  }
};

// Typing effect for alert message
const typingEffect = () => {
  if (typingEffectRunning.value) return;

  typingEffectRunning.value = true;
  const text = alertMessage.value;
  let i = 0;
  const speed = 80; // Typing speed
  alertMessage.value = ''; // Clear the message to start the animation

  const type = () => {
    if (i < text.length && typingEffectRunning.value) {
      alertMessage.value += text.charAt(i);
      i++;
      setTimeout(type, speed);
    } else {
      typingEffectRunning.value = false; // Reset flag
    }
  };

  showAlert.value = true;
  type();
};

// Reset state
const resetState = () => {
  showAlert.value = false;
  alertMessage.value = false;
  typingEffectRunning.value = false; // Reset typing effect state
};

// Modal close handler
const handleClose = () => {
  resetState();
};


</script>

<template>
  <section class="py-10">
    <h2 class="text-3xl font-bold mb-8 ml-10">Contact Me</h2>

    <!-- Alert Modal -->
    <div v-if="showAlert" @click="handleClose" class="fixed inset-0 bg-blur-sm flex justify-center items-center z-50">
      <div 
        class="border border-primary-300 border-opacity-50 p-14 rounded-md shadow-lg max-w-lg text-center" 
        @click.stop
        :class="alertType === 'error' ? 'bg-messages-error' : 'bg-messages-success' "
      >
        <p class="text-xl font-pixelify font-semibold text-primary-300">{{ alertMessage }}</p>
      </div>
    </div>
    <!-- alert itself-->
    <div :class="{'blur-sm': showAlert}" class="grid grid-cols-1 lg:grid-cols-2 md:grid-cols-1 max-w-7xl mx-auto border border-borders-grey rounded-md p-4 bg-sections-contact_me">

    <!-- First Column (Largest - acts as a title) -->
      <div class="first_column m-2 lg:border-r border-borders-grey border-opacity-30">
        <h3 class="uppercase underline mb-4">social media</h3>

        <!-- the social media buttons-->
        <div class="flex flex-col gap-6 min-w-[350px] mt-16 ml-0">
          <!-- <div >
            <a target="_blank" aria-label="linkedin" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2 ">
                <img src="/linkedin.svg" alt="Linkedin" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">linkedin</h3>
              </div>
              <p class="pl-3 capitalize">currently no linkedin</p>
            </a>
          </div> -->

          <div class="">
            <a href="mailto:levinsonvaleri@gmail.com" aria-label="Email" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2 ">
                <img src="/email.svg" alt="email" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">email</h3>
              </div>
              <p class="pl-3">levinsonvaleri@gmail.com</p>
            </a>
          </div>

          <!-- <div>
            <a aria-label="facebook" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2 ">
                <img src="/facebook1.svg" alt="facebook" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">facebook</h3>
              </div>
              <p class="pl-3 capitalize">currently no facebook</p>
            </a>
          </div> -->

          <div class="">
            <a  aria-label="phone call" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2">
                <img src="/phone_call.svg" alt="phone call" class="w-6 h-6" >
                <h3 class="pt-1 uppercase ">phone number</h3>
              </div>
              <p class="pl-3 capitalize">+972 0552251273</p>
            </a>
          </div>

          <div>
            <a 
              href="/valerilevinson_CV.pdf" 
              download="CV.pdf"
              class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2 ">
                <img src="/cv.svg" alt="cv_image" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">Download CV</h3>
              </div>
            </a>
          </div>
        </div>
      </div>

      <!-- Second Column: Send Message -->
      <div class="second_column ml-4 m-6">
        <h3 class="uppercase underline mb-4">leave a message</h3>
        <div class="space-y-4 items-center">
          <!-- form section -->
          <div class="max-w-lg mx-auto p-0 lg:p-6 md:p-6 shadow-md rounded-lg">
            <form @submit.prevent="sendMessage">
              <!-- Name -->
              <div class="mb-4">
                <label for="name" class="block mb-2 text-sm font-roboto text-primary-300">Name</label>
                <input
                  type="text"
                  id="name"
                  v-model="formData.name"
                  class="w-full border border-borders-grey bg-borders-grey bg-opacity-20 p-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                  placeholder="Your Name"
                  required
                />
              </div>

              <!-- Email -->
              <div class="mb-4">
                <label for="email" class="block mb-2 text-sm font-roboto text-primary-300">Email</label>
                <input
                  type="email"
                  id="email"
                  v-model="formData.email"
                  class="w-full border border-borders-grey bg-borders-grey bg-opacity-20 p-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                  placeholder="Your Email"
                  required
                />
              </div>

              <!-- Phone -->
              <div class="mb-4">
                <label for="phone" class="block mb-2 text-sm font-roboto text-primary-300">Phone (optional)</label>
                <input
                  type="tel"
                  id="phone"
                  v-model="formData.phone"
                  class="w-full border border-borders-grey bg-borders-grey bg-opacity-20 p-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                  placeholder="Your Phone"
                />
              </div>

              <!-- Message -->
              <div class="mb-6">
                <label for="message" class="block mb-2 text-sm font-roboto text-primary-300">Message</label>
                <textarea
                  id="message"
                  v-model="formData.message"
                  class="w-full border border-borders-grey bg-borders-grey bg-opacity-20 p-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                  placeholder="Your Message"
                  rows="4"
                  required
                ></textarea>
              </div>

              <!-- Submit Button -->
               <button
               :disabled="buttonDisabled"
                data-callback="sendMessage"
                data-action="submit"
                class="g-recaptcha flex justify-center gap-4 w-full bg-buttons-success bg-opacity-80 text-primary-300 py-2 px-4 rounded-md shadow-md hover:bg-buttons-success focus:ring-0 focus:ring-borders-green focus:ring-opacity-50"
              >
              <div v-if="buttonDisabled" class="w-6 h-6 border-4 border-blue-500 border-t-transparent rounded-full animate-spin">
              </div>
                Send Message
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.blur-sm {
  backdrop-filter: blur(8px);
}
</style>
