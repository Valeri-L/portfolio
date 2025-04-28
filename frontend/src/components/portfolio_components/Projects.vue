<script setup>
import { ref } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Pagination, Navigation } from 'swiper/modules'; // <-- added Navigation
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';   // <-- added this
import 'swiper/css/effect-coverflow';

// Data for the "projects" section
const projects = ref([
  {
    folder: 'tickettracker',
    images: ['ticket_1.png', 'ticket_2.png', 'ticket_test.png'],
    title: 'Ticket Manager',
    text: 'fullstack web application designed to help organizations efficiently manage their operational tasks through an intuitive ticketing system.',
    buttons: [
      { button_text: "read more", url: "/documentation/valar_crm" },
      { button_text: "visit application", url: "https://ticket-tracker.valar.software.com" }
    ]
  },
  {
    folder: 'crm',
    images: ['crm_1.png', 'crm_2.png', 'crm_3.png'],
    title: 'valar CRM',
    text: 'A free Customer Relationship Management (CRM) portal tailored for small businesses. Designed for simplicity, security, and speed, it features an intuitive user interface and visually appealing graphical insights.',
    buttons: [
      { button_text: "read more", url: "/documentation/valar_crm" },
      { button_text: "see demo", url: "https://crm.valerilevinson.com" }
    ]
  },
  {
    folder: 'weatherapp',
    images: ['weather_1.png','weather_2.png', 'weather_3.png'],
    title: 'weather API comparison',
    text: 'A Weather API Comparison application that highlights discrepancies between two forecasting APIs, demonstrating how online data can sometimes be inaccurate.',
    buttons: [
      { button_text: "read more", url: "/documentation/weather_api" },
      { button_text: "view on GIT", url: "https://github.com/valeri-l/weather_representation" }
    ]
  },
  {
    folder: 'topdown',
    images: ['topdown_2.jpg', 'topdown_3.jpg','fighter_test.png'],
    title: 'top down fighter',
    text: 'A top-down fighter game featuring smooth FPS handling, intense battles against monsters and bosses, brought to life with beautifully crafted pixel art assets.',
    buttons: [
      { button_text: "read more", url: "/documentation/top_down" },
      { button_text: "view on GIT", url: "https://github.com/valeri-l/fighter" }
    ]
  }
]);

</script>

<template>
  <section class="projects py-10">
    <h2 class="text-3xl text-start mb-8 ml-10">Projects</h2>
    
    <div class="border p-6 border-borders-green bg-sections-projects rounded-lg">
      <Swiper
        :modules="[Pagination,Navigation]"
        effect="coverflow"
        :grabCursor="true"
        :centeredSlides="true"
        :slidesPerView="1"
        :spaceBetween="0"
        :pagination="{ clickable: true }"
        :navigation="true"
        :coverflowEffect="{
          rotate: 50,
          stretch: 0,
          depth: 300,
          modifier: 1,
          slideShadows: true
        }"

        
        class="max-w-[1400px] w-full mx-auto"
      >

      <SwiperSlide v-for="(item, index) in projects" :key="index">
        <div class="flex flex-col mx-10 mb-10 h-full items-center justify-between">
          
          <!-- Three images overlapping -->
          <div class="relative w-full h-[200px] md:h-[300px] flex justify-center items-center overflow-visible mb-6">
            <img 
              v-for="(img, imgIndex) in item.images"
              :key="imgIndex"
              :src="`/projects/${item.folder}/${img}`"
              :alt="`Image ${imgIndex+1}`"
              :class="[
                'absolute md:static w-24 md:w-52 rounded-lg border border-gray-400 transition-transform duration-300 hover:scale-105',
                imgIndex === 0 ? 'md:translate-x-[26px] md:translate-y-[22px]' : '',
                imgIndex === 1 ? 'md:translate-x-[16px] md:translate-y-[-16px]' : '',
                imgIndex === 2 ? 'md:translate-y-[16px]' : '',
              ]"
            />
          </div>

          <!-- Title and description -->
          <div>
            <h3 class="font-semibold text-primary-300 mb-2 text-center">{{ item.title }}</h3>
            <p class="text-primary-300 text-center mx-4 max-w-xl leading-relaxed">{{ item.text }}</p>
          </div>

          <!-- Buttons -->
          <div class="pt-5 flex flex-wrap justify-center">
            <div v-for="(button, idx) in item.buttons" :key="idx">
              <a class="m-1" :href="button.url" target="_blank" rel="noopener noreferrer">
                <button class="bg-buttons-success font-pixelify text-primary-300 capitalize py-1 px-3 focus:outline-none focus:ring-0 hover:bg-opacity-80 transition">
                  {{ button.button_text }}
                </button>
              </a>
            </div>
          </div>

        </div>
      </SwiperSlide>

    </Swiper>
  </div>
  </section>
</template>

<style scoped>
  .swiper-pagination {
    margin-top: 20px;
    text-align: center;
  }
  .swiper-slide {
    transform: translateY(50px);
    opacity: 0;
    transition: all 0.6s ease;
  }

  .swiper-slide-active,
  .swiper-slide-duplicate-active {
    transform: translateY(0);
    opacity: 1;
  }
</style>
