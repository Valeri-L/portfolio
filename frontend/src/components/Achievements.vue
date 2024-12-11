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
    <section class="achievements-section py-10">
    <h2 class="text-3xl font-bold mb-8">Achievements</h2>
    <div class="grid grid-cols-1 lg:grid-cols-4 md:grid-cols-3 gap-4 max-w-7xl mx-auto border border-borders-green rounded-md p-4 bg-sections-achievements">
      <!-- First Column (Largest) -->
      <div class="md:col-span-2 flex justify-center items-center">
        <div>
            <h3 class="capitalized mb-4">leetcode</h3>
        
        <img 
          src="/leetcode.png" 
          alt="Achievement" 
          class="w-full h-auto object-contain max-h-[500px] shadow-lg"
        />
        </div>
      </div>

      <!-- Second Column (Small Placeholder) -->
      <div class="md:col-span-1 flex flex-col lg:border-r border-borders-green border-opacity-30 p-4  shadow-md">
        <div class="space-y-4 text-center">
          <!-- Titles and Stats -->
          <div>
            <h4 class="text-lg font-bold text-text-purple uppercase">total solved</h4>
            <p class="font-pixelify text-md">42</p>
          </div>
          <div>
            <h4 class="text-lg font-bold text-text-red uppercase">hard</h4>
            <p class="font-pixelify text-md">18</p>
          </div>
          <div>
            <h4 class="text-lg font-bold text-text-yellow uppercase">medium</h4>
            <p class="font-pixelify text-md">12</p>
          </div>
          <div>
            <h4 class="text-lg font-bold text-text-green uppercase">easy</h4>
            <p class="font-pixelify text-md">12</p>
          </div>
        </div>
      </div>

      <!-- Divider -->
      <!-- <div class="hidden md:block border-l border-borders-green"></div> -->


      <!-- Third Column (GitHub Stats) -->
      <div class="lg:col-span-1 md:col-span-3 text-center p-4 shadow-md border-t lg:border-none md:border-t border-borders-green">
        <h3 class=" font-bold mb-4 ">GitHub</h3>
        <!-- Year 2024 -->
        <h5 class="text-lg font-semibold">2024</h5>
        <p class="text-sm ">GitHub Commits - 444</p>
        <p class="text-sm ">Projects Done - 4</p>

        <!-- Spacer -->
        <div class="my-8"></div>

        <!-- Year 2023 -->
        <h5 class="text-lg font-semibold">2023</h5>
        <p class="text-sm">GitHub Commits - 123</p>
        <p class="text-sm ">Projects Done - 2</p>
      </div>

            <!-- <div class="hidden md:block absolute inset-y-0 left-2/3 w-px bg-gray-300"></div> -->

    </div>
  </section>

</template>

<style scoped>

</style>
