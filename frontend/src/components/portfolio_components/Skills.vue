<script setup>
import { ref } from 'vue'
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
  
    <section class="skills-section p-10 my-6">
        <h2 class="text-3xl font-bold text-start my-6">Skills</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-5xl mx-auto">
            <div 
                v-for="skill in skills" 
                :key="skill.name" 
                class="flex items-start space-x-3">
            <img 
            :src="`/skills/${skill.image}.png`" 
            :alt="skill.name" 
            class="h-8 object-contain"
            />
                <h4 class="text-lg font-medium text-">{{ skill.name }}</h4>
            </div>
        </div>
    </section>

</template>

<style scoped>

</style>
