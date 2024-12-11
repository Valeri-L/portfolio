<script setup>
import { ref } from 'vue'

// Data for the "projects" section
const projects = ref([
  {
    image: 'valar_crm',
    title: 'valar CRM',
    text: 'with PostgreSQL, MySQL, and MongoDB databases. I also use tools like Docker, AWS, and NGINX to ensure secure, efficient, and reliable application deployment.',
    button_text:"see demo",
    url:"https://crm.valerilevinson.com"
  },
  {
    image: 'weather_api',
    title: 'weather API comparison',
    text: 'with PostgreSQL, MySQL, and MongoDB databases. I also use tools like Docker, AWS, and NGINX to ensure secure, efficient, and reliable application deployment.',
    button_text:"view on GIT",
    url:"https://github.com/hayhuhin/weather_representation"  
},
  {
    image: 'top_down',
    title: 'top down fighter',
    text: 'with PostgreSQL, MySQL, and MongoDB databases. I also use tools like Docker, AWS, and NGINX to ensure secure, efficient, and reliable application deployment.',
    button_text:"view on GIT",
    url:"https://github.com/hayhuhin/fighter"  
},
]);

</script>

<template>
    <!-- <h3 class="capitalize">skills</h3> -->
  
    <section class="projects py-10">
    <h2 class="text-3xl text-start mb-8 ml-10">Projects</h2>
    <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-3 gap-8 max-w-6xl border p-4 border-borders-green bg-sections-projects rounded-lg">
      <!-- Single Column -->
      <div 
        v-for="(item, index) in projects" 
        :key="index" 
        :class="['flex flex-col items-center justify-between  xl:border-r lg:border-r sm:border-r-none border-borders-green border-opacity-30',{ 'border-none': index === projects.length - 1 }]" 
        
        >
        <!-- Image -->
        <img 
          :src="`/projects/${item.image}.png`" 
          :alt="item.title" 
          class="h-60 object-contain mb-4"
        />
        <!-- Title -->
        <h3 class="font-semibold text-primary-300 mb-2 text-center">{{ item.title }}</h3>
        <!-- Description -->
        <p class="text-primary-300 text-center mx-4 max-w-xl leading-relaxed">{{ item.text }}</p>
        <a class="m-4" :href="item.url" target="_blank">
            <button class="bg-buttons-success font-pixelify  text-primary-300 capitalize py-1 focus:outline-none focus:ring-0">{{ item.button_text }}</button>
        </a>
      </div>
    </div>
  </section>

</template>

<style scoped>

</style>
