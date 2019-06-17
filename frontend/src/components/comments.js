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
        fetch(`http://localhost:8000/api/v1/comments/?blog_post=${this.props.id}`)
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
                      <article class="media comments-box">
                        <div class="media-content">
                            <div class="content">
                            <p>
                                <strong>{ comment.name }</strong>
                                <br />
                                { comment.comment_body }
                            </p>
                            </div>
                            <nav class="level is-mobile">
                            <div class="level-left">
                            </div>
                            </nav>
                        </div>
                      </article>
                    ))}
                </section>
            )
        }
    }
}

export default Comments;