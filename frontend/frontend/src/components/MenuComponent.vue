<template>
  <div class="container mt-4">
    <!-- Top Menus (Horizontal) -->
    <div class="menu">
      <ul class="nav nav-tabs">
        <li v-for="menu in menus" :key="menu.name" class="nav-item">
          <a
            href="#"
            class="nav-link"
            :class="{ active: selectedMenu === menu.name }"
            @click="selectMenu(menu)"
          >
            {{ menu.name }}
          </a>
        </li>
      </ul>
    </div>

    <!-- Submenus (Vertical) -->
    <div v-if="selectedMenu" class="submenu mt-3">
      <ul class="list-group">
        <li
          v-for="submenu in selectedMenuSubmenus"
          :key="submenu"
          class="list-group-item"
        >
          <a
            href="#"
            @click="selectSubmenu(submenu)"
            class="text-decoration-none"
          >
            {{ submenu }}
          </a>
        </li>
      </ul>
    </div>

    <!-- Dynamic Content Section -->
    <div class="content mt-4" id="main">
      <component :is="currentComponent"></component>
    </div>
  </div>
</template>

<script>
// Import the components that you want to display dynamically
import PatientDetailsForm from "./PatientDetailsForm.vue";

export default {
  data() {
    return {
      menus: [],
      selectedMenu: "",
      selectedSubmenu: "",
      currentComponent: null, // The current component to display in the "main" div
    };
  },
  computed: {
    selectedMenuSubmenus() {
      const selected = this.menus.find(
        (menu) => menu.name === this.selectedMenu
      );
      return selected ? selected.submenus : [];
    },
  },
  methods: {
    selectMenu(menu) {
      this.selectedMenu = menu.name;
      this.selectedSubmenu = ""; // Reset the submenu when a new menu is selected

      // Determine the component to load based on the selected menu
      if (menu.name === "Patients") {
        this.currentComponent = "PatientDetailsForm"; // Load the patient details form
      } else {
        this.currentComponent = null; // Clear the component if there's no matching content
      }
    },
    selectSubmenu(submenu) {
      this.selectedSubmenu = submenu;

      // Add logic here to handle submenu selection and load appropriate components
    },
  },
  mounted() {
    // Simulating JSON data fetch
    this.menus = [
      {
        name: "Patients",
        submenus: [
          "patient-contacts",
          "dental-information",
          "medical-information",
        ],
      },
      { name: "Appointments", submenus: [] },
      { name: "Payments", submenus: [] },
      { name: "Reports", submenus: [] },
      { name: "Admin", submenus: [] },
      { name: "Lab", submenus: [] },
    ];
  },
  components: {
    PatientDetailsForm, // Register the component so it can be used dynamically
  },
};
</script>

<style>
.menu ul {
  margin-bottom: 0; /* Remove margin from ul */
}

.submenu ul {
  margin-top: 10px;
}

.content {
  margin-top: 20px;
}
</style>
