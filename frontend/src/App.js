import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'
import Footer from './components/footer/Footer.js'
//import './components/footer/style.css'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
        'authors': []
        }
    }

//    componentDidMount() {
//        const authors = [
//            {
//                'first_name': 'Фёдор',
//                'last_name': 'Достоевский',
//                'birthday_year': 1821
//            },
//            {
//                'first_name': 'Александр',
//                'last_name': 'Грин',
//                'birthday_year': 1880
//            },
//                ]
//            this.setState(
//                    {
//                        'authors': authors
//                    }
//                )
//        }
//        render () {
//            return (
//            <div>
//                <AuthorList authors={this.state.authors} />
//            </div>
//            )
//        }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                    'authors': authors
                    }
                )
            }).catch(error => console.log(error))
        }
        render () {
            return (
            <div>
                <AuthorList authors={this.state.authors} />
                < Footer/>
            </div>
            )
        }
}



export default App;