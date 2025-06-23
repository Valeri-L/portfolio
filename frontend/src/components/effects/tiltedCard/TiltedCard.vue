
<template>
    <div
      class="tilted-card-figure"
      :style="{ width: containerWidth, height: containerHeight }"
      @mousemove="handleMouseMove"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
    >
      <!-- Mobile warning (shown only if `showMobileWarning` && isMobile) -->
      <div
        v-if="showMobileWarning && isMobile"
        class="tilted-card-mobile-alert"
      >
        Mobile tilt effect is disabled
      </div>
  
      <!-- Inner 3D container that actually tilts & scales -->
      <div
        ref="inner"
        class="tilted-card-inner"
        :style="innerStyle"
      >
        <!-- Render any passed‐in content via default slot -->
        <slot>
          
        </slot>
      </div>
  
      <!-- Caption / tooltip (fades in on hover) -->
      <div v-if="showTooltip" class="tilted-card-caption">
        {{ captionText }}
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onBeforeUnmount, computed } from 'vue'
  
  // ------------------------
  // Props (similar to before, but no more imageSrc etc.)
  // ------------------------
  const props = defineProps({
    captionText: {
      type: String,
      default: '',
    },
    containerHeight: {
      type: String,
      default: '300px',
    },
    containerWidth: {
      type: String,
      default: '300px',
    },
    rotateAmplitude: {
      type: Number,
      default: 12,
    },
    scaleOnHover: {
      type: Number,
      default: 1.2,
    },
    showMobileWarning: {
      type: Boolean,
      default: true,
    },
    showTooltip: {
      type: Boolean,
      default: true,
    },
  })
  
  const inner = ref(null)
  const isHovering = ref(false)
  const tiltX = ref(0)
  const tiltY = ref(0)
  const scale = ref(1)
  const isMobile = ref(false)
  
  // ------------------------
  // Detect mobile (<=640px) to optionally disable tilt
  // ------------------------
  function updateIsMobile() {
    isMobile.value = window.innerWidth <= 640
  }
  onMounted(() => {
    updateIsMobile()
    window.addEventListener('resize', updateIsMobile)
  })
  onBeforeUnmount(() => {
    window.removeEventListener('resize', updateIsMobile)
  })
  
  // ------------------------
  // Mouse event handlers
  // ------------------------
  function handleMouseEnter() {
    if (props.showMobileWarning && isMobile.value) return
    isHovering.value = true
    scale.value = props.scaleOnHover
  }
  
  function handleMouseLeave() {
    isHovering.value = false
    tiltX.value = 0
    tiltY.value = 0
    scale.value = 1
  }
  
  function handleMouseMove(evt) {
    if (props.showMobileWarning && isMobile.value) return
  
    const el = inner.value
    const { left, top, width, height } = el.getBoundingClientRect()
    const posX = evt.clientX - left
    const posY = evt.clientY - top
  
    const offsetX = (posX / width) - 0.5
    const offsetY = (posY / height) - 0.5
  
    // Invert X so moving right tilts left and vice versa (optional)
    tiltY.value = offsetX * props.rotateAmplitude * -1
    tiltX.value = offsetY * props.rotateAmplitude
  }
  
  // ------------------------
  // Computed style for `.tilted-card-inner`
  // ------------------------
  const innerStyle = computed(() => {
    return {
      transform: `perspective(800px)
                  rotateX(${tiltX.value}deg)
                  rotateY(${tiltY.value}deg)
                  scale(${scale.value})`,
      transition: isHovering.value
        ? 'transform 0.1s ease-out'
        : 'transform 0.5s ease-out',
    }
  })
  </script>
  
  <style scoped>
  /* The container that sets perspective and centers children */
  .tilted-card-figure {
    position: relative;
    width: 100%;
    height: 100%;
    perspective: 800px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  /* Mobile-warning banner */
  .tilted-card-mobile-alert {
    position: absolute;
    top: 1rem;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.875rem;
    background: rgba(255, 255, 255, 0.9);
    color: #333;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    z-index: 10;
    display: none;
  }
  @media (max-width: 640px) {
    .tilted-card-mobile-alert {
      display: block;
    }
    .tilted-card-caption {
      display: none; /* hide tooltip on small screens */
    }
  }
  

  .tilted-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
  }
  
  /* Caption (tooltip) that fades in on hover */
  .tilted-card-caption {
    pointer-events: none;
    position: absolute;
    bottom: 1rem;
    left: 50%;
    transform: translateX(-50%);
    background-color: rgba(255, 255, 255, 0.9);
    color: #2d2d2d;
    padding: 0.25rem 0.75rem;
    font-size: 0.875rem;
    border-radius: 4px;
    opacity: 0;
    z-index: 5;
    transition: opacity 0.3s ease-in-out;
  }
  .tilted-card-figure:hover .tilted-card-caption {
    opacity: 1;
  }
  </style>
  