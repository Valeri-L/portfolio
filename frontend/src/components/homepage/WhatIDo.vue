<script setup>
import { computed } from 'vue'
import { useLanguage } from '../../composables/useLanguage'
import FadeContent from '../effects/fadeContent/FadeContent.vue'
import ScrollReveal from '../effects/scrollReveal/ScrollReveal.vue'

const { lang, getText } = useLanguage()

const whatIDoItems = computed(() => getText('whatIDo.items'))
const sectionTitle = computed(() => getText('whatIDo.title'))
</script>

<template>
  <section class="what-i-do-section">
    <!-- Section heading stays as-is or you can fade that too if you want -->
    <h2 class="text-3xl text-start mb-8 ml-10" :dir="lang==='he'?'rtl':'ltr'">
      {{ sectionTitle }}
    </h2>

    <!-- Stacked list of items -->
    <div
      class="flex flex-col gap-8 max-w-6xl p-4  mx-auto"
    >
      <!-- Wrap each card in FadeContent -->
      <FadeContent
        v-for="(item, index) in whatIDoItems"
        :key="index"
        className="border-borders-purple border-opacity-30 border border-borders-purple rounded-lg bg-sections-what_i_do bg-opacity-10"
        :blur="true"
        :duration="1600"
        easing="ease-out"
        :delay="index * 200"
        :threshold="1"
        initialOpacity="0"
      >
        <div
          :class="[
            'flex flex-col',
            { 'border-none': index === whatIDoItems.length - 1 }
          ]"
        >
          <img
            :src="`/what_i_do/${item.image}.png`"
            :alt="item.title"
            class="h-60 object-contain mb-4"
          />

          <h3
            class="font-semibold text-primary-300 mb-2 text-start"
            :dir="lang==='he'?'rtl':'ltr'"
          >
            {{ item.title }}
          </h3>

          <!-- <ScrollReveal>
          <p
            class="text-primary-300 mx-4 max-w-xl leading-relaxed"
            :dir="lang==='he'?'rtl':'ltr'"
          >
            {{ item.text }}
          </p>
        </ScrollReveal> -->
        <ScrollReveal :text="item.text" />

        </div>
      </FadeContent>
    </div>
  </section>
</template>



<style scoped>

</style>
