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
      class="mb-6 px-4"
      :dir="lang === 'he' ? 'rtl' : 'ltr'"
    >
      {{ sectionTitle }}
    </h2>

    <div class="section_container">
      <!-- yOffset="2" -->
      <div
        v-for="(item, index) in whatIDoItems"
        :key="index"
        class="ninja-clipper"       
      >

      <img
          :src="index % 2 === 0 ? '/running-right.gif' : '/running-left.gif'"
          alt="Running Ninja"
          class="ninja"
          :class="index % 2 === 0 ? 'run-right' : 'run-left'"
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
          class="text_image_container"
          :class="{ 'flex-row-reverse text-left': index % 2 === 1 }"
        >
        
        <!-- Text block -->
        <div class="flex flex-col max-w-[50rem]">
          <h3
            class="font-semibold text-primary-300 text-start mb-2 underline"
            :dir="lang === 'he' ? 'rtl' : 'ltr'"
            >
            {{ item.title }}
          </h3>
          <ScrollReveal
            :text="item.text"
            class="w-full"
            />
          </div>

          <!-- handling the gif/video that inside the card -->
          <component
            :is="item.image.endsWith('.mp4') ? 'video' : 'img'"
            :src="`/what_i_do/${item.image}`"
            v-bind="item.image.endsWith('.mp4') 
              ? { autoplay: true, muted: true, loop: true, class: 'gif_component' } 
              : { alt: item.title, class: 'gif_component' }"
          />
            </div>
          </div>
        </FadeContent>
      </div>
    </div>
  </section>
</template>



<style scoped>
.ninja-clipper {
  position: relative;
  /* overflow-x: hidden;
  overflow-y: visible; */
}

/* common ninja styling */
.ninja {
  position: absolute;
  top: -5rem;
  width: 5rem;
  pointer-events: none;
  z-index: 10;
}

/* run → right */
@keyframes ninja-run-right {
  0%   { left: -20rem; }
  15%  { left: calc(100% + 20rem); }
  100% { left: calc(100% + 20rem); }
}
.run-right {
  animation: ninja-run-right 30s linear infinite backwards;
}

/* run ← left */
@keyframes ninja-run-left {
  0%   { left: calc(100% + 20rem); }
  15%  { left: -20rem; }
  100% { left: -20rem; }
}
.run-left {
  top: -6.8rem;
  width: 8rem;
  animation: ninja-run-left 30s linear infinite backwards;
}

/* your card styling */
.expertise-cards {
  position: relative;
  border: 1px solid rgba(139,92,246,0.3);
  border-radius: 0.5rem;
  background-color: rgba(99,102,241,0.1);
  padding: 2.5rem;
  width: 100%;
}

/* text-4xl text-center mb-8 ml-10 */

.what-i-do-section {
  
}

.section_container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;

}

.text_image_container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: start;
    gap: 1.2rem;
    /* flex flex-row justify-between items-start */
  }

  
.gif_component {
  height: auto;
  object-fit: contain;
  /* margin-bottom: 2rem; */
  /* h-60 object-contain mb-4 */
}

/* DESKTOP WIDTH HANDLING */
@media (min-width:1024px) {
  .what-i-do-section {    
    .h2 {
      font-size: .4rem;
    }
  }

  .text_image_container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: start;
    gap: 1.2rem;
    /* flex flex-row justify-between items-start */
  }

  .section_container {
    display: flex;
    flex-direction: column;
    gap: 2rem;

  }
  .gif_component {
    height: 12rem;
    object-fit: contain;
    margin-bottom: 4rem;
    /* h-60 object-contain mb-4 */
  }

}


</style>



