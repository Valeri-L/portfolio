<template>
  <div class="skills-section">
    <h2 class="text-3xl font-bold text-center mb-6 text-white">
      {{ getText('skills.title') }}
    </h2>

    <!-- Phone/tablet: native dropdown -->
    <div class="tab-select-wrapper">
      <select v-model="activeTab" class="tab-select">
        <option v-for="tab in tabs" :key="tab" :value="tab">
          {{ tab.toUpperCase() }}
        </option>
      </select>
    </div>

    <!-- Desktop: pill nav + animated list -->
    <div class="nav-animated-list-wrapper">
      <nav class="tab-nav">
        <button
          v-for="tab in tabs"
          :key="tab"
          @click="activeTab = tab"
          :class="[
            'px-4 py-2 rounded-full whitespace-nowrap transition-colors font-pixelify',
            activeTab === tab
              ? 'bg-borders-purple text-white'
              : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
          ]"
        >
          {{ tab.toUpperCase() }}
        </button>
      </nav>

      <AnimatedList
        :key="activeTab"
        :items="filteredSkills"
        :showGradients="true"
        :enableArrowNavigation="true"
        :maxPerColumn="5"
        class="mt-6"
        @select="onSkillSelect"
      >
        <template #default="{ item }">
          <a
            :href="item.url"
            target="_blank"
            rel="noopener"
            class="animated-list-img-p-wrapper"
          >
            <img
              :src="`/skills/${item.image}.png`"
              :alt="item.name"
              class="h-8 w-8 flex-shrink-0"
            />
            <span class="text-lg font-pixelify">{{ item.name }}</span>
          </a>
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
  {
    image: 'python',
    name: 'Python',
    category: 'backend',
    url: 'https://docs.python.org/3/'
  },
  {
    image: 'fastapi',
    name: 'FastAPI',
    category: 'backend',
    url: 'https://fastapi.tiangolo.com/'
  },
  {
    image: 'django',
    name: 'Django',
    category: 'backend',
    url: 'https://docs.djangoproject.com/en/stable/'
  },
  {
    image: 'nextjs',
    name: 'NextJS',
    category: 'frontend',
    url: 'https://nextjs.org/docs'
  },
  {
    image: 'react',
    name: 'React',
    category: 'frontend',
    url: 'https://reactjs.org/docs/getting-started.html'
  },
  {
    image: 'html',
    name: 'HTML',
    category: 'frontend',
    url: 'https://developer.mozilla.org/en-US/docs/Web/HTML'
  },
  {
    image: 'sass',
    name: 'SASS',
    category: 'frontend',
    url: 'https://sass-lang.com/documentation'
  },
  {
    image: 'css',
    name: 'CSS',
    category: 'frontend',
    url: 'https://developer.mozilla.org/en-US/docs/Web/CSS'
  },
  {
    image: 'tailwind',
    name: 'Tailwind',
    category: 'frontend',
    url: 'https://tailwindcss.com/docs'
  },
  {
    image: 'figma',
    name: 'Figma',
    category: 'ui/ux',
    url: 'https://help.figma.com/hc/en-us'
  },
  {
    image: 'aws',
    name: 'AWS',
    category: 'devops',
    url: 'https://docs.aws.amazon.com/'
  },
  {
    image: 'docker',
    name: 'Docker',
    category: 'devops',
    url: 'https://docs.docker.com/'
  },
  {
    image: 'github',
    name: 'GitHub',
    category: 'other',
    url: 'https://docs.github.com/'
  },
  {
    image: 'mongodb',
    name: 'MongoDB',
    category: 'other',
    url: 'https://docs.mongodb.com/'
  },
  {
    image: 'mysql',
    name: 'MySQL',
    category: 'other',
    url: 'https://dev.mysql.com/doc/'
  },
];


const filteredSkills = computed(() => {
  return activeTab.value === 'all'
    ? allSkills
    : allSkills.filter(s => s.category === activeTab.value)
})
</script>

<style scoped>
.skills-section {
  max-height: 50rem;
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
