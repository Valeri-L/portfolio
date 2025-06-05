<script setup>
import { ref } from 'vue'
import { useLanguage } from '../../composables/useLanguage'
import ScrollVelocity from '../effects/scrollVelocity/ScrollVelocity.vue';

const { lang, getText } = useLanguage()

const skills = ref([
  { image: 'python', name: 'Python' },
  { image: 'javascript', name: 'JavaScript' },
  { image: 'aws', name: 'Amazon Web Services' },
  { image: 'django', name: 'Django' },
  { image: 'react', name: 'React' },
  { image: 'docker', name: 'Docker' },
  { image: 'github', name: 'Git' },
  { image: 'html', name: 'HTML' },
  { image: 'mongoDB', name: 'MongoDB' },
  { image: 'pygame', name: 'Pygame' },
  { image: 'css', name: 'CSS' },
  { image: 'mysql', name: 'MySQL' },
  
]);

</script>

<template>
    <!-- <h3 class="capitalize">skills</h3> -->
  
    <section class="skills-section p-10 my-6 bg-gray-900">
    <h2 
      class="text-3xl font-bold text-start my-6 text-white" 
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
        :items="skills"
        :baseVelocity="-100"
        :itemWidth="200"
      />
    </div>
  </section>

</template>

<style scoped>
.skills-section > div + div {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
</style>
