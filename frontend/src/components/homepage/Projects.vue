<script setup>
import { computed } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Pagination, Navigation } from 'swiper/modules'
import { useLanguage } from '../../composables/useLanguage'

import 'swiper/css'
import 'swiper/css/pagination'
import 'swiper/css/navigation'
import 'swiper/css/effect-coverflow'

const { lang, getText } = useLanguage()

const projects = computed(() => getText('projects.list'))
const sectionTitle = computed(() => getText('projects.title'))
</script>

<template>
<section class="projects py-10">
  <h2 class="text-3xl text-start mb-8 ml-10" :dir="lang === 'he' ? 'rtl' : 'ltr'">{{ sectionTitle }}</h2>

  <div class="border p-6 border-borders-green bg-sections-projects rounded-lg">
    <Swiper
      :modules="[Pagination,Navigation]"
      effect="coverflow"
      :grabCursor="true"
      :centeredSlides="true"
      :slidesPerView="1"
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

          <div>
            <h3 class="font-semibold text-primary-300 mb-2 text-center" :dir="lang === 'he' ? 'rtl' : 'ltr'">{{ item.title }}</h3>
            <p class="text-primary-300 text-center mx-4 max-w-xl leading-relaxed" :dir="lang === 'he' ? 'rtl' : 'ltr'">{{ item.text }}</p>
          </div>

          <div class="pt-5 flex flex-wrap justify-center">
            <div v-for="(button, idx) in item.buttons" :key="idx">
              <a class="m-1" :href="button.url" target="_blank" rel="noopener noreferrer">
                <button class="bg-buttons-success font-pixelify text-primary-300 capitalize py-1 px-3 focus:outline-none focus:ring-0 hover:bg-opacity-80 transition" :dir="lang === 'he' ? 'rtl' : 'ltr'">
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
