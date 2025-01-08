<script setup>
    import { ref,shallowRef, watch } from 'vue';
    import { useRoute } from 'vue-router';

    import DocCRM from './documentation_componenets/DocCRM.vue';
    import DocTopDown from './documentation_componenets/DocTopDown.vue';
    import DocWeatherAPI from './documentation_componenets/DocWeatherAPI.vue';
    import DocNavigationBar from './documentation_componenets/DocNavigationBar.vue';
    import NotFound from './documentation_componenets/NotFound.vue';
    import InDevelopment from './error_componenets/InDevelopment.vue';

    // Map the parameter to specific components
    const documentationComponents = {
        valar_crm: DocCRM, // DocCRM,
        top_down: InDevelopment, //DocTopDown,
        weather_api: InDevelopment, //DocWeatherAPI,
      };
    
    const route = useRoute(); // Access the current route
    const component = shallowRef(documentationComponents[route.params.project] || NotFound);
    
    // Watch for route changes and update the component
    watch(() => route.params.project, (newProject) => {
        component.value = documentationComponents[newProject] || null;
    });
</script>


<template>
    <div>
        <header class="fixed top-0 left-0 w-full z-10">
        <DocNavigationBar />
        </header>

        <div class="mt-[180px]">
            <!-- <h1>Documentation Page</h1> -->
            <component :is="component" />
        </div>
    </div>
  </template>
  
  
  <style scoped>
  /* Optional styling */
  </style>
  