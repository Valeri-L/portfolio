<template>
    <div ref="containerRef" class="marquee-container overflow-hidden w-full">
      <div 
        ref="innerRef" 
        class="marquee-inner flex"
        :style="innerStyle "
      >
        <div
          v-for="(skillObj, i) in visibleItems"
          :key="i"
          class="skill-item flex-shrink-0 flex items-center justify-center space-x-2"
          :style="{ width: itemWidth + 'px' }"
        >
          <img 
            :src="`/skills/${skillObj.image}.png`" 
            :alt="skillObj.name" 
            class="h-8 w-8 object-contain" 
          />
          <span class="text-lg font-medium text-white">{{ skillObj.name }}</span>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
  
  /**
   * Props:
   * - items: Array<{ image: String, name: String }>
   * - baseVelocity: Number (px/sec). Positive = left→right, Negative = right→left.
   * - itemWidth: Number (px) — fixed width for each skill slot.
   */
  const props = defineProps({
    items: {
      type: Array,
      required: true
    },
    baseVelocity: {
      type: Number,
      default: 60 
    },
    itemWidth: {
      type: Number,
      default: 120 
    }
  })
  
  const containerRef = ref(null)
  const innerRef = ref(null)
  
  const containerWidth = ref(0)
  const visibleCount = ref(1)   // how many slots we render
  
  // Circular buffer state:
  const startIndex = ref(0)     // which index in props.items sits at the leftmost rendered slot
  const offsetX = ref(0)        // pixel offset; we’ll initialize this to –itemWidth
  
  // Variables for scroll‐velocity tracking:
  let prevScrollY = window.scrollY
  let prevTime = performance.now()
  
  let animationFrameId
  
  /**
   * Measure how many items we need to render to fill the container + 1 extra
   */
  function updateContainerSize() {
    if (!containerRef.value) return
    containerWidth.value = containerRef.value.offsetWidth
    visibleCount.value = Math.ceil(containerWidth.value / props.itemWidth) + 1
  }
  
  onMounted(async () => {
    // Wait a tick so the DOM has rendered and we can measure accurately
    await nextTick()
    updateContainerSize()
    window.addEventListener('resize', updateContainerSize)
  
    // ** Initialize offsetX so the first item sits off‐screen on the left **
    offsetX.value = -props.itemWidth
  
    // Start the animation loop
    prevTime = performance.now()
    prevScrollY = window.scrollY
    animationFrameId = requestAnimationFrame(animateFrame)
  })
  
  onBeforeUnmount(() => {
    window.removeEventListener('resize', updateContainerSize)
    cancelAnimationFrame(animationFrameId)
  })
  
  watch(
    () => props.items.length,
    () => {
      // If items array changes length, reset to safe defaults
      startIndex.value = 0
      offsetX.value = -props.itemWidth
    }
  )
  
  /**
   * Modulo for negative‐friendly wraparound:
   */
  function mod(v, n) {
    return ((v % n) + n) % n
  }
  
  /**
   * The main loop: track scroll‐velocity, compute a horizontal shift,
   * adjust offsetX, and wrap the buffer index whenever one slot fully scrolls by.
   */
  function animateFrame(timestamp) {
    const delta = timestamp - prevTime
    const currentScrollY = window.scrollY
  
    // 1) Compute vertical scroll speed (px/sec)
    const scrollVel = ((currentScrollY - prevScrollY) * 1000) / (delta || 16)
    prevScrollY = currentScrollY
    prevTime = timestamp
  
    // 2) For now, we just use baseVelocity directly (no scroll‐modulation)
    const moveBy = props.baseVelocity * (delta / 1000)
  
    // 3) Update offsetX
    offsetX.value += moveBy
  
    // 4) Wrap when one slot’s width has scrolled fully
    const W = props.itemWidth
    if (offsetX.value >= W) {
      offsetX.value -= W
      startIndex.value = mod(startIndex.value - 1, props.items.length)
    }
    else if (offsetX.value <= -W) {
      offsetX.value += W
      startIndex.value = mod(startIndex.value + 1, props.items.length)
    }
  
    animationFrameId = requestAnimationFrame(animateFrame)
  }
  
  /**
   * Build exactly `visibleCount` items, starting from `startIndex`,
   * wrapping around the original `items` array in a circular fashion.
   */
  const visibleItems = computed(() => {
    const N = props.items.length
    const out = []
    for (let i = 0; i < visibleCount.value; i++) {
      out.push(props.items[ mod(startIndex.value + i, N) ])
    }
    return out
  })
  
  /**
   * Inline style for the inner flex container: translateX by offsetX px.
   */
   const innerStyle = computed(() => ({
  transform: `translateX(${offsetX.value - props.itemWidth + 20}px)`
}))

  </script>
  
  <style scoped>
  .marquee-container {
    position: relative;
    width: 100%;
    
  }
  
  .marquee-inner {
    display: flex;
    align-items: center;
    white-space: nowrap;
  }
  
  .skill-item {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 80px;           
    box-sizing: border-box;
    padding: 0 1rem;        /* space between icon and text */
  }
  </style>
  