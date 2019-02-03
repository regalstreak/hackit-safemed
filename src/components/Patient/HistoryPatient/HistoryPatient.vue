<template>
  <div>
    <div>
      <v-toolbar color="teal" dark tabs class="pt-2">
        <v-text-field
          append-icon="mic"
          class="mx-3"
          flat
          label="Search"
          prepend-inner-icon="search"
          solo-inverted
        ></v-text-field>

        <v-tabs
          grow
          slot="extension"
          v-model="tabs"
          centered
          color="transparent"
          slider-color="white"
        >
          <v-tab>Medical Records</v-tab>
          <v-tab>uploaded Files</v-tab>
        </v-tabs>
      </v-toolbar>

      <v-tabs-items v-model="tabs">
        <v-tab-item>
          <medical-records-patient></medical-records-patient>
        </v-tab-item>
        <v-tab-item>
          <uploaded-files-patient></uploaded-files-patient>
        </v-tab-item>
      </v-tabs-items>
    </div>

    <v-bottom-nav :active.sync="bottomNav" :value="true" fixed>
      <v-btn color="teal" @click="homeClicked" flat value="home">
        <span>Home</span>
        <v-icon>home</v-icon>
      </v-btn>

      <v-btn color="teal" @click="qrClicked" flat value="QR">
        <span>QR</span>
        <v-icon>texture</v-icon>
      </v-btn>

      <v-btn color="teal" @click="historyClicked" flat value="history">
        <span>History</span>
        <v-icon>history</v-icon>
      </v-btn>

      <v-btn color="teal" @click="accountClicked" flat value="account">
        <span>Account</span>
        <v-icon>person</v-icon>
      </v-btn>
    </v-bottom-nav>
  </div>
</template>

<script>
import store from "../../../store.js";
import MedicalRecordsPatient from "./MedicalRecordsPatient";
import UploadedFilesPatient from "./UploadedFilesPatient";
export default {
  data() {
    return {
      tabs: null,
      text:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    };
  },

  components: {
    "medical-records-patient": MedicalRecordsPatient,
    "uploaded-files-patient": UploadedFilesPatient
  },

  methods: {
    homeClicked() {
      this.$store.commit("changeBottomNavState", "home");
      this.$router.push("/patient");
    },
    qrClicked() {
      this.$store.commit("changeBottomNavState", "QR");
      this.$router.push("/patient/qr");
    },
    historyClicked() {
      this.$store.commit("changeBottomNavState", "history");
      this.$router.push("/patient/history");
    },
    accountClicked() {
      this.$store.commit("changeBottomNavState", "account");
      this.$router.push("/patient/account");
    }
  },
  computed: {
    bottomNav: {
      get() {
        return store.getters.bottomNavState;
      },
      set() {}
    }
  }
};
</script>

<style>
</style>
