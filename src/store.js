import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    bottomNavState: "home",
    contractAddressState: "",
    patientAddressState: "",
    changePatient: false

  },
  mutations: {
    changeBottomNavState(state, bottomNavState) {
      state.bottomNavState = bottomNavState;
    },
    changeContractAddressState(state, contractAddressState) {
      state.contractAddressState = contractAddressState;
    },
    changePatientAddressState(state, patientAddressState) {
      state.patientAddressState = patientAddressState;
    },
    mutateChangePatient(state, changePatient) {
      state.changePatient = changePatient;
    },
  },
  getters: {
    bottomNavState: state => state.bottomNavState,
    contractAddressState: state => state.contractAddressState,
    patientAddressState: state => state.patientAddressState,
    changePatient: state => state.changePatient,
  },
  actions: {

  }
})
