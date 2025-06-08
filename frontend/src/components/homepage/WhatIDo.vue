<script setup>
import { computed } from 'vue'
import { useLanguage } from '../../composables/useLanguage'
import FadeContent from '../effects/fadeContent/FadeContent.vue'
import ScrollReveal from '../effects/scrollReveal/ScrollReveal.vue'

const { lang, getText } = useLanguage()

const whatIDoItems = computed(() => getText('whatIDo.items'))
const sectionTitle = computed(() => getText('whatIDo.title'))
const delays = whatIDoItems.value.map(() => Math.random() * 30)
</script>
<template>
  <section class="what-i-do-section">
    <h2
      class="text-4xl text-center mb-8 ml-10"
      :dir="lang === 'he' ? 'rtl' : 'ltr'"
    >
      {{ sectionTitle }}
    </h2>

    <div class="flex flex-col gap-8">
      <!-- yOffset="2" -->
      <div
        v-for="(item, index) in whatIDoItems"
        :key="index"
        class="ninja-clipper"       
      >

      <img
          src="/running-ninja.gif"
          alt="Running Ninja"
          class="ninja"
          :style="{ animationDelay: `${delays[index]}s` }"
        />       

        <FadeContent
          class-name="expertise-cards"
          :blur="true"
          :duration="1000"
          easing="ease-in-out"
          :delay="index * 90"
          initial-opacity="0"
          :y-offset="150"
        >

   
        <div
          class="flex flex-col"
          :class="{ 'border-none': index === whatIDoItems.length - 1 }"
        >
          <div
            class="flex flex-row justify-between items-start"
            :class="{ 'flex-row-reverse text-left': index % 2 === 1 }"
          >
            <!-- Text block -->
            <div class="flex flex-col max-w-[50rem]">
              <h3
                class="font-semibold text-primary-300 text-start mb-[2rem]"
                :dir="lang === 'he' ? 'rtl' : 'ltr'"
              >
                {{ item.title }}
              </h3>
              <ScrollReveal
                :text="item.text"
                class="w-full"
              />
            </div>

            <!-- handling the gif/video  -->
            <component
              :is="item.image.endsWith('.mp4') ? 'video' : 'img'"
              :src="`/what_i_do/${item.image}`"
              v-bind="item.image.endsWith('.mp4') 
                ? { autoplay: true, muted: true, loop: true, class: 'h-60 object-contain mb-4' } 
                : { alt: item.title, class: 'h-60 object-contain mb-4' }"
            />
          </div>
        </div>
      </FadeContent>
    </div>
    </div>
  </section>
</template>




<style scoped>
/* 1) Clip wrapper: hides the ninja when off-screen */
.ninja-clipper {
  position: relative;
  /* overflow: hidden; */
}

/* 2) Your card styles — no overflow here */
.expertise-cards {
  position: relative;
  border: 1px solid rgba(139, 92, 246, 0.3);    /* border-borders-purple@30% */
  border-radius: 0.5rem;                        /* rounded-lg */
  background-color: rgba(99, 102, 241, 0.1);    /* bg-sections-what_i_do@10% */
  padding: 2.5rem;                              /* p-10 */
  width: 100%;
}

/* 3) Keyframes for a quick run then long pause */
@keyframes ninja-run {
  0%   { left: -20rem; }
  15%  { left: calc(100% ); }
  100% { left: calc(100% ); }
}

/* 4) The ninja itself */
.ninja {
  position: absolute;
  top: -5rem;                              /* lift above the card */
  left: -20rem;                            /* start fully off-screen */
  width: 5rem;                             /* your gif width */
  pointer-events: none;
  animation: ninja-run 30s linear infinite backwards;
}
</style>


