import { Component } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Album} from "../models";
import {AlbumService} from "../album.service";
import { Albums} from "../fake-db";
import{ HttpClient } from "@angular/common/http";
import{ Location} from "@angular/common";

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent {

  album: Album;
  albums: Album[];
  newTitle: string;
  loaded: boolean;

  constructor(private route: ActivatedRoute,
              private postService: AlbumService,
              private albumService: AlbumService,
              private http: HttpClient,
              private location: Location) {
    this.albums = [];
    this.album = {} as Album;
    this.loaded = true;
    this.newTitle = "";
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      let _id = params.get('id');
      if (_id) {
        let id = +_id;
        this.loaded = false;
        this.postService.getAlbum(id).subscribe((album) => {
          this.album = album;
          this.loaded = true;
        })
      }
    });
  }
  saveAlbum(){
    this.album.title = this.newTitle;

    this.http.put(`https://jsonplaceholder.typicode.com/albums/${this.album.id}`, this.album);
  }

  getPhotos(){
    this.route.paramMap.subscribe((params) => {
      let _id = params.get('id');
      if (_id) {
        let id = +_id;
        this.loaded = false;
        this.postService.getPhotos(id).subscribe((album) => {
          this.album = album;
          this.loaded = true;
        })
      }
    });
  }

  deleteAlbum(){

  }

  goBack(): void {
    this.location.back();
  }
}

