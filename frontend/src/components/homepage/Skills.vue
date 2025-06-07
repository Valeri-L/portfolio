<script setup>
import { ref } from 'vue'
import { useLanguage } from '../../composables/useLanguage'
import ScrollVelocity from '../effects/scrollVelocity/ScrollVelocity.vue';

const { lang, getText } = useLanguage()

const skills = ref([
  { image: 'python', name: 'Python' },
  { image: 'javascript', name: 'JavaScript' },
  { image: 'django', name: 'Django' },
  { image: 'react', name: 'React' },
  { image: 'html', name: 'HTML' },
  { image: 'css', name: 'CSS' },

  
]);


const skills2 = ref([
  { image: 'github', name: 'Git' },
  { image: 'pygame', name: 'Pygame' },
  { image: 'docker', name: 'Docker' },
  { image: 'aws', name: 'AWS' },
  { image: 'mongoDB', name: 'MongoDB' },
  { image: 'mysql', name: 'MySQL' },
  
]);

</script>

<template>
    <!-- <h3 class="capitalize">skills</h3> -->
  
    <div class="skills-section  mb-[10rem] ">
    <h2 
      class="text-3xl font-bold text-center mb-6 text-white" 
      :dir="lang === 'he' ? 'rtl' : 'ltr'"
    >
      {{ getText('skills.title') }}
    </h2>

    <!-- Top line scrolls left-to-right (baseVelocity=+80) -->
 <!-- Top line: scrolls left→right -->
 <div class="mb-6">
      <ScrollVelocity
        :items="skills"
        :baseVelocity="100"
        :itemWidth="200"
      />
    </div>

    <!-- Bottom line: scrolls right→left -->
    <div class="mt-6">
      <ScrollVelocity
        :items="skills2"
        :baseVelocity="-100"
        :itemWidth="200"
      />
    </div>
  </div>

</template>

<style scoped>
.skills-section > div + div {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
</style>
