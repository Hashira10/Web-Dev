import { Component } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Album} from "../models";
import {PostService} from "../post.service";

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent {

  post: Album;
  loaded: boolean;

  constructor(private route: ActivatedRoute,
              private postService: PostService) {
    this.post = {} as Album;
    this.loaded = true;
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      let _id = params.get('id');
      if (_id) {
        let id = +_id;
        this.loaded = false;
        this.postService.getPost(id).subscribe((post) => {
          this.post = post;
          this.loaded = true;
        })
      }
    });
  }
}
