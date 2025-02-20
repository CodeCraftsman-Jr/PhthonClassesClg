import React from 'react'
import './Content.css'

const Content = () => {
  const greetlist = ['Hello','Hi'];
  const rand = Math.floor(Math.random() * greetlist.length);
  const greet = greetlist[rand];
  return (
    <section className="content">
      <div className="content-container">
        <h1>{greet},Welcome to My Website</h1>
        <p>
          Hello guys i am vasanthan from sri venkateshwaraa college of enginerring and technology puducherry/
        </p>
        <p>
          This is a sample content page we created using react  click on the below button to see our day 4 heart animation project using Event Listener
        </p>
        <button className="cta-button" onClick={() => window.location.href = '/index.html'}>Learn More</button>
        <h1>This is to change the Greeting on Button click </h1>
        <h1>Click on the below button to change the greeting</h1>
        <button className="cta-button">Change Greeting</button>
      </div>
    </section>
  )
}

export default Content
