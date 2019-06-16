import React, { Component } from 'react';
import Moment from 'react-moment';
import { Link } from 'react-router-dom';
import './css/blog.css';

const MAX_LENGTH = 50;
class Blog extends Component {

    constructor(props) {
        super(props);
        this.state = {
            posts: [],
            isLoaded: false,
        }
    };

    componentDidMount() {

        fetch('http://localhost:8000/api/v1/blog_post/')
            .then(res => res.json())
            .then(json => {
                this.setState({
                    isLoaded: true,
                    posts: json,
                });
            });
    };

    

    render() {
        var { isLoaded, posts } = this.state;
        if (!isLoaded) {
            return (
                <div>Loading...</div>
            )
        }

        else {

            return(

                <div id="posts" class="clearfix">
                  {posts.map(post => (
                    <figure class="post card">
                        <div class="card-image">
                        <div class="image is-3by2">
                        <img class="" src={post.images} />
                        </div>
                        </div>
                        <figcaption class="card-body">
                        <h2>{post.title}</h2>
                        {post.post.length > MAX_LENGTH ?
                            (
                            <div>
                                {`${post.post.substring(0, MAX_LENGTH)}...`}
                            </div>
                            ) :
                            <p>{post.post}</p>
                        }
                        </figcaption>
                        <Link to={`/blog/${post.id}`} title="Read more">Read more</Link>
                    </figure>
                    ))}
                </div>
            )
        }
    }
}

export default Blog;