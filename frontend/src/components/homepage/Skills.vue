<template>
  <div class="skills-section ">
    <h2 class="text-3xl font-bold text-center mb-6 text-white">
      {{ getText('skills.title') }}
    </h2>

    <!-- Phone/tablet: native dropdown -->
    <div class="tab-select-wrapper">
      <select v-model="activeTab" class="tab-select">
        <option
          v-for="tab in tabs"
          :key="tab"
          :value="tab"
        >
          {{ tab.toUpperCase() }}
        </option>
      </select>
    </div>

    <!-- Desktop: scrollable pill buttons -->
     <div class="nav-animated-list-wrapper">
      <nav class="tab-nav">
        <button
          v-for="tab in tabs"
          :key="tab"
          @click="activeTab = tab"
          :class="[
            'px-4 py-2 rounded-full whitespace-nowrap transition-colors font-pixelify Pixelify',
            activeTab === tab
              ? 'bg-borders-purple text-white'
              : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
          ]"
        >
          {{ tab.toUpperCase() }}
        </button>
      </nav>

    <!-- AnimatedList-->

      <AnimatedList
        :key="activeTab"
        :items="filteredNames"
        :showGradients="true"
        :enableArrowNavigation="true"
        :maxPerColumn="5"
        class="mt-6"
        @select="(item, idx) => console.log('selected', item, idx)"
      >
        <template #default="{ item }">
          <div class="animated-list-img-p-wrapper">
            <img
              :src="`/skills/${item.toLowerCase()}.png`"
              :alt="item"
              class="h-8 w-8 flex-shrink-0"
            />
            <span class="text-lg font-pixelify Pixelify">{{ item }}</span>
          </div>
        </template>
      </AnimatedList>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useLanguage } from '../../composables/useLanguage'
import AnimatedList from '../effects/animatedList/AnimatedList.vue'

const { lang, getText } = useLanguage()

const tabs      = ['all','frontend','ui/ux','backend','devops','other']
const activeTab = ref('all')

const allSkills = [
  { image: 'python',    name: 'Python',       category: 'backend' },
  { image: 'fastapi',   name: 'FastAPI',      category: 'backend' },
  { image: 'django',    name: 'Django',       category: 'backend' },
  { image: 'nextjs',    name: 'Next.js',      category: 'frontend' },
  { image: 'react',     name: 'React',        category: 'frontend' },
  { image: 'html',      name: 'HTML',         category: 'frontend' },
  { image: 'css',       name: 'CSS',          category: 'frontend' },
  { image: 'tailwind',  name: 'Tailwind',     category: 'frontend' },
  { image: 'figma',     name: 'Figma',        category: 'ui/ux' },
  { image: 'aws',       name: 'AWS',          category: 'devops' },
  { image: 'docker',    name: 'Docker',       category: 'devops' },
  { image: 'github',    name: 'GitHub',       category: 'other'   },
  { image: 'mongodb',   name: 'MongoDB',      category: 'other'   },
  { image: 'mysql',     name: 'MySQL',        category: 'other'   },
]

const filteredNames = computed(() => {
  const list = activeTab.value === 'all'
    ? allSkills
    : allSkills.filter(s => s.category === activeTab.value)
  return list.map(s => s.name)
})
</script>

<style scoped>
.skills-section {
  height: 100vh;
}

.nav-animated-list-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.2rem;
}

.tab-select-wrapper {
  display: none;
}

/* pill-style nav */
.tab-nav {
  display: flex;
  /* justify-content: center; */
  gap: 0.5rem;
  overflow-x: auto;
  padding: .2rem 1.2rem;
  scrollbar-width: none;
}
.tab-nav::-webkit-scrollbar {
  display: none;
}

/* dropdown on small screens */
@media (max-width: 640px) {
  .tab-nav {
    display: none;
  }
  .tab-select-wrapper {
    display: block;
    margin-bottom: 1rem;
    text-align: center;
  }
  .tab-select {
    @apply px-4 py-2 bg-gray-700 text-gray-300 ;
  }
  .animated-list-img-p-wrapper {
    flex-direction: column;
    margin: 0rem;
    padding: 0rem;
    
  }
}

.animated-list-img-p-wrapper {
  @apply 
    flex items-center 
    space-x-2 m-2 px-4 py-[1rem] 
    border rounded-[1rem] 
    whitespace-nowrap 
    transition-colors bg-gray-700 text-gray-300 hover:bg-gray-600;
}


</style>
