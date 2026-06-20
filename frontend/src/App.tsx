import React, { useState } from 'react'

export default function App() {
  const [location, setLocation] = useState('')
  const [climb, setClimb] = useState('')
  const [result, setResult] = useState<string | null>(null)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const res = await fetch('/api/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ location, climb })
      })

      if (!res.ok) {
        const text = await res.text()
        setResult(`Error: ${res.status} ${text}`)
        return
      }

      const data = await res.json()
      // show returned JSON (adjust according to backend shape)
      setResult(JSON.stringify(data))
    } catch (err: any) {
      setResult(`Network error: ${err?.message ?? err}`)
    }
  }

  return (
    <div style={{padding:20,fontFamily:'sans-serif'}}>
      <h1>Climb Recommender</h1>
      <form onSubmit={submit} style={{display:'grid',gap:10,maxWidth:400}}>
        <label>
          Location
          <input value={location} onChange={e=>setLocation(e.target.value)} placeholder="e.g. Yosemite" />
        </label>

        <label>
          Climb
          <input value={climb} onChange={e=>setClimb(e.target.value)} placeholder="e.g. El Capitan" />
        </label>

        <button type="submit">Submit</button>
      </form>

      {result && (
        <div style={{marginTop:20}}>
          <strong>Result</strong>
          <div>{result}</div>
        </div>
      )}
    </div>
  )
}
