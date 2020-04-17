import React from 'react'


export default class Hasil extends React.Component{
    constructor(props){
        super(props)
        this.digit = props.isi.digit;
        this.kalimat = props.isi.kalimat;
        this.namafile = props.isi.nama;
        this.id = props.isi.id;
    }

    render(){
        return(
            <div>
                <div>
                    <div>
                        {this.id+1}.                                                               
                    </div>
                    <div>
                        File : {this.namafile}
                    </div>
                </div>
                <div>
                    Jumlah : {this.digit ? this.digit : "No Digit"}
                </div>
                <div>
                    Kalimat : {this.kalimat}
                </div>
            </div>
        )
    }
}