<script setup>
import { ref } from 'vue'

// Data for the "What I Do" section
const whatIDoItems = ref([
  {
    image: 'backend',
    title: 'backend development',
    text: 'The backbone of any high-performing application is a well-designed and efficient backend. My expertise spans designing database schemas, developing and optimizing RESTful APIs, setting up efficient routing mechanisms, creating custom middleware, and implementing comprehensive unit tests to ensure reliability and high performance.As a strong Python advocate, I specialize in using Django and Flask to build scalable, secure, and maintainable web APIs. I am proficient in working with both SQL databases like MySQL and NoSQL databases like MongoDB, ensuring the right solution is tailored to each project’s unique requirements.',
  },
  {
    image: 'fullstack',
    title: 'full stack development',
    text: 'On the frontend, I like to create seamless and visually appealing interfaces using tools like React, Material-UI, Bootstrap, Nivo Charts, and Chart.js. For design, I rely on Figma to craft modern and intuitive user experiences that enhance usability and engagement.On the backend, I build robust and scalable systems using Django, Django REST Framework, and Flask, integrating with PostgreSQL, MySQL, and MongoDB databases. I also use tools like Docker, AWS, and NGINX to ensure secure, efficient, and reliable application deployment.',
  },
  {
    image: 'networking',
    title: 'networking',
    text: 'I have a deep understanding of the networking infrastructures required to support fully functional applications. With extensive knowledge of networking protocols, I can design, implement, and troubleshoot systems to ensure seamless communication and optimal performance.My expertise includes working with firewalls (Cisco, Fortinet, Check Point, Juniper), DNS management, and implementing secure, scalable network solutions. Leveraging AWS, I deploy and manage cloud-based services to ensure reliability, scalability, and cost efficiency for modern applications.This blend of networking and cloud expertise allows me to build and maintain robust environments for both backend systems and full-stack applications.',
  },
]);

</script>

<template>
    <!-- <h3 class="capitalize">skills</h3> -->
  
    <section class="what-i-do-section py-10">
    <h2 class="text-3xl text-start mb-8 ml-10">What I Do</h2>
    <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-3 gap-8 max-w-6xl p-4 border border-borders-purple rounded-lg bg-sections-what_i_do bg-opacity-10">
      <!-- Single Column -->
      <div 
        v-for="(item, index) in whatIDoItems" 
        :key="index" 
        :class="['flex flex-col xl:border-r lg:border-r sm:border-r-none border-borders-purple border-opacity-30',{ 'border-none': index === whatIDoItems.length - 1 }]" 
      >
      
        <!-- Image -->
        <img 
          :src="`/what_i_do/${item.image}.png`" 
          :alt="item.title" 
          class="h-60 object-contain mb-4"
        />
        <!-- Title -->
        <h3 class="font-semibold text-primary-300 mb-2 text-start">{{ item.title }}</h3>
        <!-- Description -->
        <p class="text-primary-300 mx-4 max-w-xl leading-relaxed">{{ item.text }}</p>
      </div>
    </div>
  </section>

</template>

<style scoped>

</style>
