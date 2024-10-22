import Image from 'next/image'
import Header from './components/Layout/Navbar'
import Intro from './pages/Intro'

export default function Home() {
  return (
    <main className='bg-white'>
      <Header/>
      <Intro/>
    </main>
  )
}
