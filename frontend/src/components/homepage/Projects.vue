<script setup>
import { computed } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Pagination, Navigation } from 'swiper/modules'
import { useLanguage } from '../../composables/useLanguage'
import FadeContent from '../effects/fadeContent/FadeContent.vue'

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
  <h2 class="text-4xl text-center mb-8 ml-10" :dir="lang === 'he' ? 'rtl' : 'ltr'">{{ sectionTitle }}</h2>
  <FadeContent
          class-name="expertise-cards"
          :blur="true"
          :duration="1000"
          easing="ease-in-out"
          :delay="index * 90"
          initial-opacity="0"
          :y-offset="150"
        >
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
        class="max-w-[140rem] w-full mx-auto"
      >
        <SwiperSlide v-for="(item, index) in projects" :key="index">
          <div class="flex flex-col mx-10 mb-10 items-center justify-between">
            <div class="relative w-full flex justify-center items-center overflow-visible mb-6">
              <div class="image-wrapper">
                <img
                  v-for="(img, imgIndex) in item.images"
                  :key="imgIndex"
                  :src="`/projects/${item.folder}/${img}`"
                  :alt="`Image ${imgIndex+1}`"
                  :class="['image', `img-${imgIndex}`]"
                />
              </div>
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
  </FadeContent>
</section>

</template>

<style scoped>
/* 1) Default (mobile/tablet) */
.image-wrapper {
  position: relative;
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: visible;
  margin-bottom: 1.5rem;
}
.image {
  width: 100%;
  height: auto;
  object-fit: contain;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  transition: transform 0.3s;
  position: static;
}
/* hide all except the zero-index */
.img-1,
.img-2 {
  display: none;
}
/* 2) Desktop overrides */
@media (min-width: 1024px) {
  .image-wrapper {
    height: 500px;
  }
  .image {
    width: auto;
    height: 14rem;
    position: absolute;
  }

  /* per-image offsets */
  .img-0 { transform: translate(15rem, 8.2rem); }
  .img-1 { transform: translate(1.6rem, 1.6rem); }
  .img-2 { transform: translate(-17rem, 9rem); }
  
  .img-1,
  .img-2 {
    display: block;
  
}
}

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
