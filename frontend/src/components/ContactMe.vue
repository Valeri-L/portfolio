<script setup>
import { ref, watchEffect,computed } from 'vue';

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
const typing = ref(false);
const typingTimeout = ref(null);
const typingEffectRunning = ref(false);


const sendMessage = async () => {
  resetState(); // Reset previous state
  // console.log("sendMessage called, modal state reset");

  try {
    const response = await fetch('YOUR_API_ENDPOINT', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ /* request payload */ }),
    });

    if (!response.ok) {
      throw new Error('Failed to send message.');
    }

    const result = await response.json();
    alertMessage.value = "Message sent successfully!";
    alertType.value ='success';
    // console.log("Success message set:", alertMessage.value);
  } catch (error) {
    console.error("Error in sendMessage:", error);
    alertMessage.value = "An error occurred. Please try again.";
    alertType.value ='error';
    // console.log("Error message set:", alertMessage.value);
  }


  // Avoid duplicate typing effect invocation
if (!typingEffectRunning.value && alertMessage.value) {
  typingEffect();
} else {
  // console.warn("Typing effect skipped: Already running or no message.");
}

};



const typingEffect = () => {
  if (typingEffectRunning.value) {
    // console.warn("Typing effect already running.");
    return;
  }

  typingEffectRunning.value = true;
  // console.log("Typing effect started");

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
      // console.log("Typing effect completed");
      typingEffectRunning.value = false; // Reset flag here
      // Automatically close modal after typing completes
      setTimeout(() => {
        resetState();
        // console.log("Modal auto-closed");
      }, 2000);
    }
  };

  showAlert.value = true;
  type();
};



const resetState = () => {
  showAlert.value = false;
  alertMessage.value = '';
  typingEffectRunning.value = false; // Reset typing effect state
  // console.log("resetState called");
};



// Modal close handler
const handleClose = () => {
  resetState();
};


const buttonDisabled = computed(() => typingEffectRunning.value);

const handleClick = () => {
  if (buttonDisabled.value) return; // Prevent further clicks

  // Disable the button
  buttonDisabled.value = true;
  console.log("Button clicked, starting animation...");

  // Simulate animation duration (4 seconds)
  setTimeout(() => {
    buttonDisabled.value = false; // Re-enable the button
    console.log("Animation completed, re-enabling button.");
  }, 4000);
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

    <div :class="{'blur-sm': showAlert}" class="grid grid-cols-1 lg:grid-cols-2 md:grid-cols-2 max-w-7xl mx-auto border border-borders-grey rounded-md p-4 bg-sections-contact_me">
      <!-- First Column (Largest) -->
      <div class="first_column m-6 lg:border-r border-borders-grey border-opacity-30">
        <h3 class="uppercase underline mb-4">social media</h3>

        <div class="flex flex-col gap-3">
          <div>
            <a href="#" target="_blank" aria-label="linkedin" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2 ">
                <img src="/linkedin.svg" alt="Linkedin" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">linkedin</h3>
              </div>
              <p class="pl-3 capitalize">my linkedin</p>
            </a>
          </div>

          <div>
            <a href="mailto:hayhuhin.new@gmail.com" aria-label="Email" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2 ">
                <img src="/email.svg" alt="email" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">email</h3>
              </div>
              <p class="pl-3">valerilevinson@gmail.com</p>
            </a>
          </div>

          <div>
            <a href="#" aria-label="facebook" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2 ">
                <img src="/facebook1.svg" alt="facebook" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">facebook</h3>
              </div>
              <p class="pl-3 capitalize">my facebook</p>
            </a>
          </div>

          <div>
            <a href="#" aria-label="phone call" class="hover:text-gray-300 text-primary-300">
              <div class="flex gap-2">
                <img src="/phone_call.svg" alt="phone call" class="w-6 h-6" >
                <h3 class="pt-1 uppercase">phone number</h3>
              </div>
              <p class="pl-3 capitalize">+972 0552251273</p>
            </a>
          </div>

        </div>
      </div>

      <!-- Second Column: Send Message -->
      <div class="second_column ml-4 m-6">
        <h3 class="uppercase underline mb-4">leave a message</h3>
        <div class="space-y-4 items-center">
          <!-- form section -->
          <div class="max-w-lg mx-auto p-6 shadow-md rounded-lg">
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
                type="submit"
                :disabled="buttonDisabled"
                class="w-full bg-buttons-success bg-opacity-80 text-primary-300 py-2 px-4 rounded-md shadow-md hover:bg-buttons-success focus:ring-0 focus:ring-borders-green focus:ring-opacity-50"
              >
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
