<script setup>
import { computed } from 'vue'
import { useLanguage } from '../../composables/useLanguage'

const { lang, getText } = useLanguage()

const whatIDoItems = computed(() => getText('whatIDo.items'))
const sectionTitle = computed(() => getText('whatIDo.title'))
</script>


<template>
  <section 
    class="what-i-do-section"

  >
    <h2 class="text-3xl text-start mb-8 ml-10" :dir="lang === 'he' ? 'rtl' : 'ltr'">{{ sectionTitle }}</h2>

    <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-3 gap-8 max-w-6xl p-4 border border-borders-purple rounded-lg bg-sections-what_i_do bg-opacity-10">
      <div 
        v-for="(item, index) in whatIDoItems" 
        :key="index" 
        :class="['flex flex-col xl:border-r lg:border-r sm:border-r-none border-borders-purple border-opacity-30',{ 'border-none': index === whatIDoItems.length - 1 }]" 
      >
        <img 
          :src="`/what_i_do/${item.image}.png`" 
          :alt="item.title" 
          class="h-60 object-contain mb-4"
        />
        <h3 class="font-semibold text-primary-300 mb-2 text-start" :dir="lang === 'he' ? 'rtl' : 'ltr'">{{ item.title }}</h3>
        <p class="text-primary-300 mx-4 max-w-xl leading-relaxed" :dir="lang === 'he' ? 'rtl' : 'ltr'">{{ item.text }}</p>
      </div>
    </div>
  </section>
</template>


<style scoped>

</style>
