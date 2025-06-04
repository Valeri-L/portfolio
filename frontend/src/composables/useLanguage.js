import { ref } from 'vue'
import en from '../languages/en.json'
import he from '../languages/he.json'

const currentLang = ref('en')

const translations = {
  en,
  he
}

function setLanguage(langCode) {
    if (translations[langCode]) {
      currentLang.value = langCode
      localStorage.setItem('lang', langCode)

    }
  }

function getText(path) {
  const keys = path.split('.')
  let value = translations[currentLang.value]
  for (const key of keys) {
    value = value?.[key]
    if (value === undefined) return ''
  }
  return value
}

function initLanguage() {
    const saved = localStorage.getItem('lang')
    if (saved && translations[saved]) {
      currentLang.value = saved
    }
  }

initLanguage()

export function useLanguage() {
  return {
    lang: currentLang,
    setLanguage,
    getText
  }
}
