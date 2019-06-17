import React, { Component } from 'react';
import About from './about';
import Comments from './comments';
import Moment from 'react-moment';
import './css/post.css';

class Post extends Component {

    constructor(props) {
        super(props);
        
        this.state = {
            post: [],
            isLoaded: false,
            postid: props.match,
            
        }
        // console.log(props)
    };

    componentDidMount() {
        const _this = this;
        fetch(`http://localhost:8000/api/v1/blog_post/${this.props.match.params.slug}`)
            .then(res => res.json())
            .then(json => {
                this.setState({
                    isLoaded: true,
                    post: json,
                });
            });
    };

    render() {
        var { isLoaded, post, postid } = this.state;
        // console.log(postid)
        if (!isLoaded) {
            return (
                <div>Loading...</div>
            )
        }

        else {

            return(
                <div className="section">
                            <About />

                    <div className="container">
                        <div className="post-body">
                          <h1 className="custom-font">{post.title}</h1>
                          <p><strong><em><Moment format="YYYY/MM/DD">{post.created}</Moment> </em> by Writerton McWriterpants
                          </strong>
                          </p>
                        <p>
                          <img className="" src={post.images}></img>
                        </p>
                        <p className="">
                            {post.post}
                        </p>
                        <Comments id={post.id} />
                        <div className="tag">
                            {post.tags}
                        </div>
                        </div>
                    </div>
                </div>
            )
        }
    }
}

export default Post;