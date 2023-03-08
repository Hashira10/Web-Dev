import { Component, OnInit} from '@angular/core';
import { Album } from "../models";
import { Albums} from "../fake-db";
import {AlbumService} from "../album.service";

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit{
  albums: Album[];
  newAlbum: Album;
  loaded: boolean;
  delAlbum: Album;
  constructor(private albumService: AlbumService) {
    this.albums = [];
    this.newAlbum = {} as Album;
    this.loaded = true;
    this.delAlbum = {} as Album;
  }
  ngOnInit(): void {
    this.getAlbums();
  }

  getAlbums(){
    this.loaded = false;
    this.albumService.getAlbums().subscribe((albums) =>{
      this.albums = albums;
      this.loaded = true;
    })
  }

  addAlbum(){
    this.loaded = false;
    this.albumService.addAlbum(this.newAlbum).subscribe((album) => {
      // this.posts.push(post);
      this.albums.unshift(album);
      this.loaded = true;
      this.newAlbum = {} as Album;
    });
  }

  deleteAlbum(id:number){

      this.albums = this.albums.filter(a => a.id !== id);
  }

}
