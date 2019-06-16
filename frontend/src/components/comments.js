import React, { Component } from 'react';
import About from './about';
import Moment from 'react-moment';

class Comments extends Component {

    constructor(props) {
        super(props);
        // console.log(props)
        this.state = {
            comments: [],
            isLoaded: false,
            
        }
        console.log(props)
    };

    componentDidMount() {
        const _this = this;
        fetch(`http://localhost:8000/api/v1/comments/`)
            .then(res => res.json())
            .then(json => {
                this.setState({
                    isLoaded: true,
                    comments: json,
                });
            });
    };

    render() {
        var { isLoaded, comments } = this.state;
        // console.log(postid)
        if (!isLoaded) {
            return (
                <div>Loading...</div>
            )
        }

        else {

            return(
                <section className="section">
                    {comments.map(comment => (
                        <div>
                  { comment.comment_body }      
                  </div>
                    ))}
                </section>
            )
        }
    }
}

export default Comments;