import { useState, useEffect } from 'react'
import './App.css'

interface PetName {
  name: string
}

function App() {
  const [petName, setPetName] = useState<string | null>(null)

  useEffect(() => {
    const fetchPetName = async () => {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/random_pet`)
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        const data: PetName = await response.json()
        setPetName(data.name)
      } catch (error) {
        console.error('Error fetching pet name:', error)
      }
    }

    fetchPetName()
  }, [])

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Random Pet Name</h1>
      {petName ? (
        <p className="text-xl">Your random pet name is: <span className="font-semibold">{petName}</span></p>
      ) : (
        <p className="text-xl">Loading...</p>
      )}
    </div>
  )
}

export default App