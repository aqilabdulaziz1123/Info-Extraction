import React from 'react'
import ReactDOM from 'react-dom'
import Hasil from './Hasil.js'

const path = require('path')


export default class MainForm extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            files : [],
            key : "",
            hasils : []
        }
        
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }    

    handleChange(event){
        // console.log(event.target.name)
        var value = event.target.name === 'files' ? (event.target.files) : event.target.value
        // console.log(value)
        this.setState({[event.target.name] : value})   
    }

    handleSubmit(){
        console.log(this.state)
        this.setState({hasils : []})
        var files = Array.from(this.state.files).map(file => file.name);
        fetch("http://localhost:5000/query",{
            method : 'post',
            headers : {'Content-type' : 'application/json'},
            body : JSON.stringify({
                'files' : files,
                'key' : this.state.key
            })
        }).then(e => e.json())
            .then(data => this.setState({hasils : data.data}))
    }

    render(){
        return (
            <div>
                <div>
                    {/* <form onChange={this.handleChange}> */}
                    {/* <div>
                    <input type="file" name="folderDir"/>
                    </div> */}
                    <div>
                        <input name="files" type="file" onChange={this.handleChange} required multiple />
                        {/* <input type="text" name="dir"/> */}
                    </div>
                    <div>
                        <input type="text" name="key" onChange={this.handleChange}/>
                    </div>
                    <div>
                        <button onClick={this.handleSubmit} name="submit">submit</button>
                    </div>
                </div>
                <div>
                    {this.state.hasils.map(hasil =>(
                        <div>
                            <Hasil key={hasil.id} isi={hasil}/>
                        </div>
                    ))}
                </div>
            </div>
        )
    }
}