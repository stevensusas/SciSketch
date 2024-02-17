// app/providers.tsx
'use client'

import { ChakraProvider } from '@chakra-ui/react'
import { extendTheme } from "@chakra-ui/react"
import '@fontsource/poppins';



const theme = extendTheme({
  colors: {
    brand: {
      100: "#2D00F7",
      200: "#8900F2",
      300: "#B100E8",
      400: "#DB00B6",
      500: "#F20089",
    },
  },
  fonts: {
    heading: `'Poppins', sans-serif`,
    body: `'Poppins', sans-serif`,
  },
});

export function Providers({ children }: { children: React.ReactNode }) {
  return <ChakraProvider theme={theme}>{children}</ChakraProvider>
}