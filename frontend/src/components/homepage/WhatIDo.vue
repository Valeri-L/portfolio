
<template>
  <section class="what-i-do-section px-4">
    <h2
      class="section-title mb-6 text-3xl font-bold"
      :dir="lang === 'he' ? 'rtl' : 'ltr'"
    >
      {{ sectionTitle }}
    </h2>

    <div class="section_container">
      <div
        v-for="(item, index) in whatIDoItems"
        :key="index"
        class="ninja-clipper"
      >
        <FadeContent
          class-name="expertise-cards"
          :blur="true"
          :duration="1000"
          easing="ease-in-out"
          :delay="index * 90"
          initial-opacity="0"
          :y-offset="150"
        >
          <img
            :src="index % 2 === 0 ? '/running-right.gif' : '/running-left.gif'"
            alt="Running Ninja"
            class="ninja"
            :class="index % 2 === 0 ? 'run-right' : 'run-left'"
            :style="{ animationDelay: `${delays[index]}s` }"
          />

          <div class="card-content">
            <div
              class="text_image_container"
              :class="{ 'reverse': index % 2 === 1 }"
              :dir="lang === 'he' ? 'rtl' : 'ltr'"
            >
              <!-- Text block -->
              <div class="text-block" :dir="lang === 'he' ? 'rtl' : 'ltr'">
                <h3 class="item-title">{{ item.title }}</h3>
                <ScrollReveal
                  :text="item.text"
                  class="item-text"

                />
              </div>
              <!-- GIF or video -->
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

<style scoped>
.what-i-do-section {
  /* optional padding at edges */
}
.section-title {
  /* your existing h2 styles */
}

/* container of all cards */
.section_container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* each card wrapper */
.expertise-cards {
  position: relative;
  border: 1px solid rgba(139, 92, 246, 0.3);
  border-radius: 0.5rem;
  background-color: rgba(99, 102, 241, 0.1);
  padding: 2.5rem;
  width: 100%;
}


/* ninja gif */
.ninja-clipper { position: relative; overflow: hidden; }
.ninja { position: absolute; top: -5rem; width: 5rem; pointer-events: none; z-index: 10; }
@keyframes ninja-run-right {
  0%   { left: -20rem; }
  15%  { left: calc(100% + 20rem); }
  100% { left: calc(100% + 20rem); }
}
.run-right { animation: ninja-run-right 30s linear infinite backwards; }
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

/* text + media wrapper */
.text_image_container {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}
.text-block {
  flex: 1;
}
.item-title {
  font-weight: 600;
  color: #e0e0e0;
  margin-bottom: .5rem;
}
.item-text { color: #ccc; }

/* gif/video sizing */
.gif_component {
  height: 100%;
  object-fit: contain;
  margin-bottom: 1rem;
}

.text-block {
  min-width: 210px;
}

/* DESKTOP LAYOUT */
@media (min-width: 1024px) {
  .gif_component {
    height: 15rem;
    object-fit: contain;
    margin-bottom: 1rem;
  }
  .section_container {
    gap: 2rem;
  }
  .text_image_container {
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
  }
  /* reverse order + align text right */
  .text_image_container.reverse {
    flex-direction: row-reverse;

  }
}
</style>
