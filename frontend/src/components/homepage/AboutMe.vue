<script setup>
import { ref, onMounted, watch, computed, nextTick } from 'vue'
import { useLanguage } from '../../composables/useLanguage'
import ShinyText from '../effects/ShinyText/ShinyText.vue'
import TiltedCard from '../effects/tiltedCard/TiltedCard.vue'

const { lang, getText } = useLanguage()

const displayText = ref('')
const currentWordIndex = ref(0)
const currentLetterIndex = ref(0)
const isDeleting = ref(false)
const finishedTyping = ref(false)

const typingSpeed = 160
const deletingSpeed = 50
const pauseBetweenWords = 700

// Make words computed so it updates reactively on language change
const words = computed(() => [
  getText('aboutMe.title'),
  getText('aboutMe.name')
])

let typingTimeout

function startTypingAnimation() {
  clearTimeout(typingTimeout)
  if (finishedTyping.value) return

  const currentWord = words.value[currentWordIndex.value]

  if (!isDeleting.value) {
    displayText.value = currentWord.substring(0, currentLetterIndex.value + 1)
    currentLetterIndex.value++

    if (currentLetterIndex.value === currentWord.length) {
      if (currentWordIndex.value === 0) {
        typingTimeout = setTimeout(() => {
          isDeleting.value = true
          startTypingAnimation()
        }, pauseBetweenWords)
        return
      } else {
        finishedTyping.value = true
        return
      }
    }
  } else {
    displayText.value = currentWord.substring(0, currentLetterIndex.value - 1)
    currentLetterIndex.value--

    if (currentLetterIndex.value === 0) {
      isDeleting.value = false
      currentWordIndex.value++
    }
  }

  typingTimeout = setTimeout(startTypingAnimation, isDeleting.value ? deletingSpeed : typingSpeed)
}

function resetTyping() {
  clearTimeout(typingTimeout)
  displayText.value = ''
  currentWordIndex.value = 0
  currentLetterIndex.value = 0
  isDeleting.value = false
  finishedTyping.value = false
  // Wait for next DOM update to get new `words` before typing
  nextTick(() => {
    startTypingAnimation()
  })
}

onMounted(() => {
  setTimeout(()=>{
    startTypingAnimation()
  },900)
})

// Watch for language change and reset typing
watch(lang, () => {
  resetTyping()
})



function splitIntoSegments(raw) {
  const segments = [];
  // This regex finds **anything inside double asterisks**, non-greedily
  const regex = /\*\*(.*?)\*\*/g;
  let lastIndex = 0;
  let match;

  while ((match = regex.exec(raw)) !== null) {
    // `match.index` is where the `**…**` begins
    if (match.index > lastIndex) {
      // Push any plain text leading up to the highlight
      segments.push({
        type: 'text',
        content: raw.slice(lastIndex, match.index),
      });
    }
    // `match[1]` is the inner text (without the ** markers)
    segments.push({
      type: 'highlight',
      content: match[1],
    });
    // Move past this match
    lastIndex = match.index + match[0].length;
  }

  // Anything left after the last highlight becomes plain text
  if (lastIndex < raw.length) {
    segments.push({
      type: 'text',
      content: raw.slice(lastIndex),
    });
  }

  return segments;
}


const processedParagraphs = computed(() => {
  // splitting all the words that passed from the json file
  const rawParas = getText('aboutMe.paragraphs');
  return rawParas.map((p) => splitIntoSegments(p));
});

</script>
<!-- border-2 border-borders-purple -->

<template>

  <div
    class="about-me-container relative  rounded-lg  "
    :dir="lang === 'he' ? 'rtl' : 'ltr'"
    >

    <TiltedCard
      containerHeight="auto"        
      containerWidth="100%"         
      :rotateAmplitude="12"
      :scaleOnHover="1.05"          
      :showMobileWarning="true"
      :showTooltip="false"          
    >
  <div class="sliding-gradient inset-0"></div>
    <div class="aboutMeContext">
      <h1 class="capitalize h-16 overflow-hidden flex items-center mb-10">
        {{ displayText }}<span class="typing-cursor ml-1"></span>
      </h1>
      <div v-for="(segments, pIndex) in processedParagraphs" :key="pIndex" class="mb-6">
        <p>
          <template v-for="(seg, i) in segments" :key="i">
            <!-- Plain text segment -->
            <span v-if="seg.type === 'text'">
              {{ seg.content }}
            </span>
            <!-- Highlighted segment → ShinyText -->
            <ShinyText
              v-else
              :text="seg.content"
              :speed="5"
              baseColor="rgba(242, 242, 242, 1)"
              shineColor="rgba(199, 120, 221, 0.6)"
              className="inline-block text-[1.3rem]"
            />
          </template>
        </p>
      </div>
    </div>
    </TiltedCard>
  </div>
  
</template>




<style scoped>
/* 1) Base highlight: a semi-transparent dark green behind each word */
.highlight {
  position: relative;
  z-index: 1; /* keeps the text above its animated background */
  display: inline-block;  
  padding: 0 0.1em;              
  border-radius: 0.15em;         
  background-color: rgba(201, 102, 45, 0.2);
  overflow: hidden;              
}

.highlight::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;


  width: 200%;
  height: 100%;


  background: linear-gradient(
    to right,
    rgba(0, 77, 0, 0)    0%,
    rgba(0, 77, 0, 0.5)  50%,
    rgba(0, 77, 0, 0)  100%
  );
  background-repeat: no-repeat;


  transform: translateX(-100%);
  z-index: -1; 
  
  animation: swipeGreen 3s linear infinite;
}

/* 3) Keyframes move the pseudo-element from –100% → 0% → +100% */
@keyframes swipeGreen {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}



@keyframes slideFromRight {
  0%  { opacity: 0;transform: translateX(20rem);}
  80% { transform: translateX(-5rem); }
  100% { opacity: 1;transform: translateX(0); }
}

@keyframes slideFromLeft {
  0%  { opacity: 0;transform: translateX(-20rem);}
  80% { transform: translateX(5rem); }
  100% { opacity: 1;transform: translateX(0); }
}

.sliding-gradient {
  position: absolute;
  background-color: rgba(199, 120, 221, 0.15);
  border: 3px solid rgba(199, 120, 221, 0.15);
  border-radius: .7rem;
  animation: slideFromRight 1.2s ease-in-out;
}

.aboutMeContext {
  color: #f2f2f2;
  z-index: 999;
  padding: 4rem 6rem;
  animation: slideFromLeft 1.2s ease-in-out;
}

.typing-cursor {
  display: inline-block;
  width: 2px;
  height: 1.5em;
  background-color: #f2f2f2;
  margin-left: 4px;
  animation: blink 1.3s steps(1, start) infinite;
}

@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}

</style>
