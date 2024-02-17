// app/layout.tsx
import { Providers } from './providers'

import '@fontsource/poppins/400.css'




export default function RootLayout({
  children,
}: {
  children: React.ReactNode,
}) {
  return (
    <html lang='en'>
      <body>
        <Providers>{children}</Providers>
      </body>
      
    </html>
  )
}