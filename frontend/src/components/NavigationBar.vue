<script setup>
import { ref } from 'vue';
// import colors from '../assets/styles/main';

const activeButton = ref(null);

const scrollTo = (section) => {
  const element = document.getElementById(section);
  if (element) {
    // Use scrollIntoView to bring the section into view
    // element.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Add a small timeout to ensure smooth scrolling completes before adjusting offset
    setTimeout(() => {
      // Adjust the scrolling offset
      const offset = -90; // Adjust this value as needed (e.g., for fixed navbar height)
      const y = element.getBoundingClientRect().top + window.pageYOffset + offset;
      window.scrollTo({ top: y, behavior: 'smooth' });
    }, 200);

    // Set the active button
    activeButton.value = section;
  }
};

const button_sx = `bg-transparent border-none hover:underline underline-offset-8 decoration-text-purple focus:outline-none focus:ring-0`;
</script>

<template>

  <nav class="fixed w-full top-0 left-0 z-50 font-pixelify border-b border-text-red border-opacity-30 bg-primary-100 bg-opacity-80">
    <div class="flex items-center justify-between px-6 py-4">
        
      <div class="flex items-center gap-8">
      <!-- logo -->
        <div class="text-xl">
            <button :class="button_sx">Valeri Levinson</button><!-- logo on the top left side -->
        </div>
        
        <div class="flex space-x-4">
            <!-- icons -->
          <a href="https://github.com/hayhuhin" target="_blank" aria-label="GitHub" class="hover:text-gray-400">
            <img src="/github.svg" alt="GitHub" class="w-6 h-6" >
          </a>
          <a href="#" target="_blank" aria-label="linkedin" class="hover:text-gray-400">
            <img src="/linkedin.svg" alt="Linkedin" class="w-6 h-6" >
          </a>
          <a href="mailto:hayhuhin.new@gmail.com" aria-label="Email" class="hover:text-gray-400">
            <img src="/email.svg" alt="GitHub" class="w-6 h-6" >
          </a> 
          <a href="https://facebook.com/" target="_blank" aria-label="facebook" class="hover:text-gray-400">
            <img src="/facebook1.svg" alt="Facebook" class="w-6 h-6" >
          </a> 
        </div>

      </div>

        <div class="flex space-x-6">
          <button
            :class="`${button_sx} ${activeButton === 'about' ? 'no-underline' : ''}`"
            @click="scrollTo('about-me')"
          >
            About Me
          </button>
          <button
            :class="`${button_sx} ${activeButton === 'what_i_do' ? 'no-underline' : ''}`"
            @click="scrollTo('what_i_do')"
          >
            What I Do
          </button>
          <button
            :class="`${button_sx} ${activeButton === 'achievements' ? 'no-underline' : ''}`"
            @click="scrollTo('achievements')"
          >
            Achievements
          </button>
          <button
            :class="`${button_sx} ${activeButton === 'projects' ? 'no-underline' : ''}`"
            @click="scrollTo('projects')"
          >
            Projects
          </button>
          <button
            :class="`${button_sx} ${activeButton === 'contact' ? 'no-underline' : ''}`"
            @click="scrollTo('contact-me')"
          >
            Contact Me
          </button>
      </div>
    </div>
  </nav>

</template>

<style scoped>

</style>
