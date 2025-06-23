<template>
    <div
      class="animated-list-container"
      tabindex="0"
      @keydown.prevent="handleKeydown"
    >
      <div v-if="showGradients" class="gradient top"    :style="{ opacity: topGradient }" />
      <div v-if="showGradients" class="gradient bottom" :style="{ opacity: bottomGradient }" />
  
      <div class="columns">
        <ul
       v-for="(column, c) in chunkedItems"
       :key="c"
       class="column"
       @scroll="handleScroll"
       :ref="el => columnRefs[c] = el"
     >
       <AnimatedItem
         v-for="(item, i) in column"
         :key="c * maxPerColumn + i"
         :index="c * maxPerColumn + i"
        :delay="i * 0.05"
         :selected="selectedIndex === c * maxPerColumn + i"
         @mouseenter="selectIndex(c * maxPerColumn + i)"
         @click="selectItem(c * maxPerColumn + i)"
       >
         <slot :item="item">{{ item }}</slot>
       </AnimatedItem>
     </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, watch } from 'vue'
  import AnimatedItem from './animatedItem.vue'
  
  const props = defineProps({
    items:                 { type: Array, default: () => [] },
    showGradients:         { type: Boolean, default: true },
    enableArrowNavigation: { type: Boolean, default: true },
    maxPerColumn:          { type: Number, default: 5 },
  })
  const emit = defineEmits(['select'])
  
  const selectedIndex = ref(-1)
  const topGradient    = ref(0)
  const bottomGradient = ref(1)
  
  // build refs array dynamically
  const columnRefs = []
  
  // split into columns
  const chunkedItems = computed(() => {
    const chunks = []
    for (let i = 0; i < props.items.length; i += props.maxPerColumn) {
      chunks.push(props.items.slice(i, i + props.maxPerColumn))
    }
    return chunks
  })
  
  // selection
  function selectIndex(i) { selectedIndex.value = i }
  function selectItem(i)  { selectedIndex.value = i; emit('select', props.items[i], i) }
  
  // scroll gradients
  function handleScroll(e) {
    const el = e.target
    const st = el.scrollTop
    const mh = el.scrollHeight - el.clientHeight
    topGradient.value    = Math.min(st / 50, 1)
    bottomGradient.value = Math.min((mh - st) / 50, 1)
  }
  
  // keyboard
  function handleKeydown(e) {
    if (!props.enableArrowNavigation) return
    if (e.key === 'ArrowDown' || (e.key === 'Tab' && !e.shiftKey)) {
      selectedIndex.value = Math.min(selectedIndex.value + 1, props.items.length - 1)
    } else if (e.key === 'ArrowUp' || (e.key === 'Tab' && e.shiftKey)) {
      selectedIndex.value = Math.max(selectedIndex.value - 1, 0)
    } else if (e.key === 'Enter' && selectedIndex.value >= 0) {
      emit('select', props.items[selectedIndex.value], selectedIndex.value)
    }
    scrollToSelected()
  }
  
  function scrollToSelected() {
    const i = selectedIndex.value
    if (i < 0) return
    const col = Math.floor(i / props.maxPerColumn)
    const idx = i % props.maxPerColumn
    const ul  = columnRefs[col]
    if (!ul) return
    const li = ul.children[idx]
    const margin = 20
    if (li.offsetTop < ul.scrollTop + margin) {
      ul.scrollTo({ top: li.offsetTop - margin, behavior: 'smooth' })
    } else if (li.offsetTop + li.clientHeight > ul.scrollTop + ul.clientHeight - margin) {
      ul.scrollTo({
        top: li.offsetTop + li.clientHeight - ul.clientHeight + margin,
        behavior: 'smooth'
      })
    }
  }
  
  // reset gradients when items change
  watch(chunkedItems, () => {
    topGradient.value    = 0
    bottomGradient.value = 1
  })
  </script>
  
  <style scoped>
  .animated-list-container {
    position: relative;
    display: flex;
    /* justify-content: center; */
    outline: none;
  }
  
  .columns {
    display: flex;
    /* gap: 2rem; */
    flex-wrap: wrap;

  }
  
  .column {
    flex: 1;
    max-height: 30rem;
    overflow-y: auto;
    padding-right: 0.5rem;
    overflow-y: auto;           /* or scroll */
    scrollbar-width: none;      /* Firefox */
    -ms-overflow-style: none;   /* IE 10+ */
  }
  
  .gradient {
    position: absolute;
    left: 0; right: 0; height: 2rem;
    pointer-events: none;
  }
  .gradient.top {
    top: 0;
    margin: 0rem 2rem 0rem 2rem;
    background: linear-gradient(to bottom, rgba(0,0,0,0.2), transparent);
  }
  .gradient.bottom {
    bottom: 0;
    margin: 0rem 2rem 0rem 2rem;
    /* background: linear-gradient(to top, rgba(0,0,0,0.2), transparent); */
  }
  </style>
  