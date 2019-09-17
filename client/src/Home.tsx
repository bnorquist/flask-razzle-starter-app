import axios from 'axios'
import React from 'react'
import './Home.css'
import logo from './react.svg'

interface State {
  name: string
}

const API_URL: string =
  process.env.NODE_ENV === 'production'
    ? 'https://save-backend.herokuapp.com/hello'
    : 'http://api.lvh.me/hello'

class Home extends React.Component<{}, State> {
  public readonly state: State = {
    name: 'Name'
  }

  public async componentDidMount() {
    try {
      const {
        data: { name }
      } = await axios.get(API_URL, {
        params: {
          name: 'LeBron'
        }
      })
      this.setState({ name })
    } catch (err) {
      console.log(err)
    }
  }

  public render() {
    const { name } = this.state
    return (
      <div className='Home'>
        <div className='Home-header'>
          <img src={logo} className='Home-logo' alt='logo' />
          <h2>Welcome to {name}'s Savings Club</h2>
        </div>
        <p className='Home-intro'>
          To get started, edit <code>src/App.js</code> or{' '}
          <code>src/Home.js</code> and save to reload.
        </p>
        <ul className='Home-resources'>
          <li>
            <a href='https://github.com/jaredpalmer/razzle'>Docs</a>
          </li>
          <li>
            <a href='https://github.com/jaredpalmer/razzle/issues'>Issues</a>
          </li>
          <li>
            <a href='https://palmer.chat'>Community Slack</a>
          </li>
        </ul>
      </div>
    )
  }
}

export default Home
