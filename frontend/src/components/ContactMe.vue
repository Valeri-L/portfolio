<script setup>
import { ref } from 'vue'

// Form data
const formData = ref({
  name: '',
  email: '',
  phone: '',
  message: ''
});

// Send Message Function
const sendMessage = async () => {
  const apiEndpoint = 'https://example.com/api/send-message'; // Replace with your API endpoint
  try {
    const response = await fetch(apiEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData.value)
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    alert('Message sent successfully!');
  } catch (error) {
    console.error('Error sending message:', error);
    alert('Failed to send the message.');
  }
};

const count = ref(0)
</script>

<template>
    <section class="achievements-section py-10">
        
    <h2 class="text-3xl font-bold mb-8">Contact Me</h2>
        
    <!-- <div class="border-solid rounded-lg border-2 border-borders-grey bg-sections-contact_me p-10"> -->
    <div class="grid grid-cols-1 lg:grid-cols-2 md:grid-cols-2 max-w-7xl mx-auto border border-borders-grey rounded-md p-4 bg-sections-contact_me">      
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
                        <p class="pl-3 capitalize ">my linkedin </p>
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


      <!-- Second Column  send message -->
      <div class="second_column ml-4 m-6">
        <h3 class="uppercase underline mb-4">leave a message</h3>
        <div class="space-y-4 items-center">

            <!-- form section -->
            <div class="max-w-lg mx-auto p-6 shadow-md rounded-lg">
                <form @submit.prevent="sendMessage">
                <!-- Name -->
                <div class="mb-4">
                    <label for="name" class="block mb-2 text-sm font-roboto text-primary-300 ">Name</label>
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
                    class="w-full bg-buttons-success bg-opacity-80 text-primary-300 py-2 px-4 rounded-md shadow-md hover:bg-buttons-success focus:ring-0 focus:ring-borders-green focus:ring-opacity-50"
                >
                    Send Message
                </button>
                </form>
            </div>

        </div>
      </div>
    </div>
<!-- </div> -->

</section>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
