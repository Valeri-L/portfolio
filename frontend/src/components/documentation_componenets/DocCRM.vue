<template>
  <h1 class="header_large"> <span class="capitalize font-bold">CRM Portal :</span> My Journey with React and Django.</h1>
    <div class="flex flex-col gap-14">
      <!-- main header -->
      <div class="introduction_section">
        <h2 class="header_medium">Introduction</h2>
        <p class="text_regular">CRM stands for Customer Relationship Management. It addresses the challenge of saving and managing client information related to their purchases or use of a company’s services/products.</p>
        <p class="text_regular">For example, if I owned a phone store, I’d want a system that tracks client purchases, monitors income and expenses, and provides insights into revenue, employee productivity, and trending products.</p>
        <p class="text_regular">A CRM consolidates multiple tools into one platform, such as sales tracking, project management, ticketing, and dashboard insights, reducing the need for separate systems and making operations more efficient.</p>
        <p class="text_regular">The potential features of a CRM are vast. It can store sales information for analysis to grow business revenue and improve customer satisfaction. It can include a ticketing system for internal or external use, depending on the product offered, as well as project management tools like task tracking and assignment, email integration, dashboard insights, and much more.</p>
        <p class="text_regular">What I find most appealing about CRMs is their ability to centralize everything in one platform, replacing the need for multiple platforms for different company aspects. For instance, in my current job, we rely on an internal ticket portal, an external ticket portal, an orders portal, a project management portal, and several others. A CRM could streamline these processes significantly.</p>
      </div>

      <div class="why_section">
        <h2 class="header_medium">Why I Built a CRM ?</h2>
        <p class="text_regular">The idea for this CRM emerged from my experiences as a networking engineer. My job often required using multiple platforms to gather small but crucial details to resolve client issues. For instance, a customer might have to wait 30 minutes while I searched for the correct service ID because they only provided a physical address or customer ID. This process was manageable for small clients with limited services, but for medium to large businesses, it became increasingly frustrating.</p>
        <p class="text_regular">I envisioned a solution where all necessary data could be consolidated into one platform, drastically reducing wait times and improving efficiency. This realization inspired me to build a CRM tailored to solve such challenges.</p>
        <p class="text_regular">Do I think my CRM is better than existing systems developed by large teams? Of course not. However, I see this as an opportunity to learn and grow as a developer. By building this project, I’m gaining invaluable experience in software design, implementation, and problem-solving, which is why I decided to pursue it.</p>
      </div>

      <div class="how_section">
        <h2 class="header_medium">how my CRM solves a problem ?</h2>
        <p class="text_regular">My CRM includes features that other platforms offer, but its key strength is continuous growth, with new features added regularly. You can view a demo here : <a class="underline underline-offset-2" href="https://crm.valerilevinson.com">CRM Portal</a></p>
      </div>
      
      <div class="better_section">
        <h2 class="header_medium">is My CRM Better ?</h2>
        <p class="text_regular">My CRM has several advantages that make it a compelling choice:</p>
        <ul class="header_ul_regular">
          <li><span class="font-semibold">It’s Free:</span> My CRM is accessible on the web, and anyone can register and use it without any subscription or hidden fees.</li>
          <li><span class="font-semibold">Continuous Updates:</span> New features are added weekly, ensuring the platform evolves to meet user needs.</li>
          <li><span class="font-semibold">User-Friendly Design:</span> A clean and intuitive interface makes it easy to navigate and use.</li>
          <li><span class="font-semibold">Efficient Backend:</span> The backend is optimized for speed and reliability, ensuring seamless performance.</li>
        </ul>
      </div>
      
      <div class="plan_section">
        <h2 class="header_medium">How i Planned the Project ?</h2>
        <p class="text_regular">Before starting, I already had experience with Python and wanted to expand my knowledge by building a complex application. I began by exploring tutorials and "how-to" videos online, which introduced me to the Django framework. Django stood out because of its built-in functionality and alignment with the MVC (Model-View-Controller) architecture, which streamlined development and can save time. However, to avoid falling into "tutorial hell," I decided to dive into the Django documentation and start coding immediately, without prior database structuring or a detailed action plan.</p>
        <p class="text_regular">This approach taught me an invaluable lesson: planning is the cornerstone of building complex applications. While coding can account for 20% of the effort, thoughtful planning and structuring often take up the remaining 80%. The initial version of my application helped me learn Django, SQL, NoSQL (MongoDB), and Django ORM. However, it became clear that the design and structure I had implemented were not suitable for medium-to-large-scale applications.</p>
        <p class="text_regular">Starting without a concrete plan taught me the critical importance of structuring applications before coding. My first iteration helped me learn Django and database management, but it wasn't scalable. I rebuilt the application with Django REST Framework and React, adopting RESTful principles for a more maintainable architecture.</p>
      </div>
      
      <div class="technologies_section">
        <h2 class="header_medium">Technologies Used</h2>
        <p class="mb-4">My CRM leverages a robust tech stack to ensure scalability, efficiency, and security. Here's a breakdown:</p>
        <ul class="list-disc list-inside space-y-4">
          <!-- Backend Section -->
          <li>
            <span class="header_ul">Backend:</span>
            <ul class="nested_ul">
              <li>
                <span class="font-semibold">Django REST Framework (Python):</span> A powerful framework for building APIs, trusted by platforms like Instagram and Spotify.</li>
              <li>
                <span class="font-semibold">Redis:</span>
                Implemented as a caching layer to improve response times for frequently accessed data.
              </li>
            </ul>
          </li>
          <!-- Frontend Section -->
          <li>
            <span class="header_ul">Frontend:</span>
            <ul class="nested_ul">
              <li>
                <span class="font-semibold">React (JavaScript):</span>
                A popular frontend library for creating dynamic single-page applications (SPAs), developed by Meta and used by Facebook, WhatsApp, and others.
              </li>
              <li>
                <span class="font-semibold">Material UI:</span>
                Provides a wide range of prebuilt components, ensuring fast and aesthetic UI development.
              </li>
              <li>
                <span class="font-semibold">Nivo Charts:</span>
                Chosen for its robust data visualization capabilities and seamless React integration.
              </li>
              <li>
                <span class="font-semibold">Figma:</span>
                Used to design interactive wireframes and UI mockups.
              </li>
            </ul>
          </li>
          <!-- Database Section -->
          <li>
            <span class="header_ul">Database:</span>
            <ul class="nested_ul">
              <li>
                <span class="font-semibold">MongoDB:</span>
                A NoSQL database ideal for handling dynamic and graph-based data structures created by users.
              </li>
              <li>
                <span class="font-semibold">SQLite:</span>
                A SQL database ideal for handling user and product information, supporting foreign key connections.
              </li>
            </ul>
          </li>
          <!-- DevOps Section -->
          <li>
            <span class="header_ul">DevOps:</span>
            <ul class="nested_ul">
              <li>
                <span class="font-semibold">Docker and Docker Hub:</span>
                Used for containerization and service separation, adding an additional layer of protection and simplifying deployment.
              </li>
              <li>
                <span class="font-semibold">NGINX:</span>
                A web server that acts as a proxy, handling communication between the frontend and backend while enhancing security.
              </li>
              <li>
                <span class="font-semibold">GitHub and GitHub Actions:</span>
                Ensures version control and implements automated testing and deployment pipelines for stable releases.
              </li>
            </ul>
          </li>
        </ul>
        <p class="text_regular">These technologies work together to create a secure, scalable, and user-friendly CRM application. If you need further details, feel free to reach out via email or through my portfolio’s contact form.</p>
      </div>
      <div class="features_section">
        <h2 class="header_medium">features</h2>
        <p class="text_regular">Current features include:</p>
        <ul class="header_ul_regular">
          <li><span class="font-semibold">Income and Expense Tracking:</span> Managers can create custom dashboards that display monthly revenue trends, expense breakdowns, and profit margins, all dynamically updated.</li>
          <li><span class="font-semibold">Permission Management:</span> Users can assign roles like Admin, Manager,Sales,Human Resources, or regular Employee, ensuring sensitive data is only accessible to authorized individuals.</li>
          <li><span class="font-semibold">Multi-Company Support:</span> A single user can seamlessly switch between companies while keeping their data isolated and secure.</li>
        </ul>
      </div>

      <div class="challenges_section">
        <h2 class="header_medium">challenges</h2>
        <ul class="header_ul_regular">
          <li><span class="font-semibold">Database Structure:</span> "I initially struggled with optimizing API response times for complex queries. By normalizing the database and implementing indexing strategies, I improved query performance significantly."</li>
          <li><span class="font-semibold">Permissions:</span> “I had to find a solution to multi company permission handling to insure that the data cannot be accessed between different companies”.</li>
          <li><span class="font-semibold">Security:</span> ” because i come from the networking and security world i know the vulnerabilities that exist and i had to enhance the framework-specific knowledge to secure the application”.</li>
          <li><span class="font-semibold">Frontend Design:</span> "As I was new to React and Material UI, I started with simple components and progressively added complexity by referring to their documentation and examples."</li>
          <li><span class="font-semibold">Deployment and CI/CD:</span> “that almost a standard for a RESTful application to be implemented with Docker and GitHub Actions for automated testing and deployment so i learned to use this tools and understand their importance ”.</li>
        </ul>
      </div>

      <div class="lessons_section">
        <h2 class="header_medium">lessons learned</h2>
        <p class="text_regular">This project deepened my understanding of API development, secure processes, and full-stack architecture. It also taught me the importance of planning large-scale applications and staying updated on emerging technologies.</p>
      </div>

      <div class="future_section">
        <h2 class="header_medium">future plans</h2>
        <p class="text_regular">Future features include advanced analytics dashboards, integration with email services, and AI-driven customer insights. I also plan to develop a mobile-responsive design.</p>
      </div>
    </div>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  /* Add any styles here */
    .header_large {
      @apply text-primary-300  font-roboto my-12
    }
    .header_medium {
      @apply text-primary-300  font-roboto font-bold my-4 capitalize
    }
    .text_regular {
      @apply text-primary-300 leading-7 font-roboto  my-4 ml-2
    }
    .nested_ul {
      @apply list-disc pl-10 space-y-2 mt-2
    }
    .header_ul {
      @apply font-bold text-lg underline underline-offset-8
    }
    .header_ul_regular {
      @apply list-disc list-outside space-y-2 ml-2
    }
  </style>
  