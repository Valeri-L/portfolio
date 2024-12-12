<script setup>
import LeetcodeTable from './leetcode_components/LeetcodeTable.vue';
import { ref, onMounted, onUnmounted } from 'vue';
import { CountUp } from 'countup.js';


const isVisible = ref(false);

onMounted(() => {
  const section = document.querySelector('.achievements-section');
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          isVisible.value = true;
          startCounting();
        } else {
          isVisible.value = false;
          resetCounting();
        }
      });
    },
    { threshold: 0.4 } // Trigger when 50% of the section is visible
  );
  observer.observe(section);
});

function startCounting() {
  const options = { duration: 5 };

  const totalSolved = new CountUp('total-solved', 42,options);
  const hard = new CountUp('hard', 18,options);
  const medium = new CountUp('medium', 12,options);
  const easy = new CountUp('easy', 12,options);
  const commits2024 = new CountUp('commits-2024', 444,options);
  const projects2024 = new CountUp('projects-2024', 4,options);
  const commits2023 = new CountUp('commits-2023', 65,options);
  const projects2023 = new CountUp('projects-2023', 2,options);

  totalSolved.start();
  hard.start();
  medium.start();
  easy.start();
  commits2024.start();
  projects2024.start();
  commits2023.start();
  projects2023.start();
}

function resetCounting() {
  document.getElementById('total-solved').innerText = '0';
  document.getElementById('hard').innerText = '0';
  document.getElementById('medium').innerText = '0';
  document.getElementById('easy').innerText = '0';
  document.getElementById('commits-2024').innerText = '0';
  document.getElementById('projects-2024').innerText = '0';
  document.getElementById('commits-2023').innerText = '0';
  document.getElementById('projects-2023').innerText = '0';
}


</script>

<template>
    <!-- <h3 class="capitalize">skills</h3> -->
    <section class="achievements-section py-10">
    <h2 class="text-3xl font-bold mb-8 ml-10">Achievements</h2>
    <div class="grid grid-cols-1 lg:grid-cols-4 md:grid-cols-3 gap-4 max-w-7xl mx-auto border border-borders-green rounded-md p-4 bg-sections-achievements">
      <!-- First Column -->
      <div class="md:col-span-2 flex justify-center items-center ">
        <LeetcodeTable />
      </div>


      <!-- Second Column (Solved Stats) -->
      <div class="md:col-span-1 flex flex-col lg:border-r border-borders-green border-opacity-30 p-4  shadow-md">
        <div class="space-y-4 text-center">
          <div>
            <h4 class="text-lg font-bold text-text-purple uppercase">Total Solved</h4>
            <p id="total-solved" class="font-pixelify text-3xl">0</p>
          </div>
          <div>
            <h4 class="text-lg font-bold text-text-red uppercase">Hard</h4>
            <p id="hard" class="font-pixelify text-3xl">0</p>
          </div>
          <div>
            <h4 class="text-lg font-bold text-text-yellow uppercase">Medium</h4>
            <p id="medium" class="font-pixelify text-3xl">0</p>
          </div>
          <div>
            <h4 class="text-lg font-bold text-text-green uppercase">Easy</h4>
            <p id="easy" class="font-pixelify text-3xl">0</p>
          </div>
        </div>
      </div>

      <!-- Third Column (GitHub Stats) -->
      <div class="lg:col-span-1 md:col-span-3 text-center p-4 shadow-md border-t lg:border-none md:border-t border-borders-green">
        <h3 class="font-bold mb-4">GitHub</h3>

        <!-- Year 2024 -->
        <h5 class="text-lg font-semibold">2024</h5>
        <div class="flex gap-4 justify-center items-center">
          <p class="font-pixelify text-1xl uppercase">commits</p>
          <p id="commits-2024" class="font-pixelify text-2xl">0</p>
        </div>
        <div class="flex gap-4 justify-center items-center">
          <p class="font-pixelify text-1xl uppercase">projects</p>
          <p id="projects-2024" class="font-pixelify text-2xl">0</p>
      </div>

        <!-- Spacer -->
        <div class="my-8"></div>

         <!-- Year 2023 -->
         <h5 class="text-lg font-semibold">2023</h5>

         <div class="flex gap-4 justify-center items-center">
          <p class="font-pixelify text-1xl uppercase">commits</p>
          <p id="commits-2023" class="font-pixelify text-2xl">0</p>
        </div>
        <div class="flex gap-4 justify-center items-center">
          <p class="font-pixelify text-1xl uppercase">projects</p>
          <p id="projects-2023" class="font-pixelify text-2xl">0</p>
      </div>

    </div>

            <!-- <div class="hidden md:block absolute inset-y-0 left-2/3 w-px bg-gray-300"></div> -->

    </div>
  </section>

</template>

<style>

</style>
