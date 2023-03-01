

import { Component } from '@angular/core';

import { Product, products } from '../products';
import {category1} from "../category";
import {ProductService} from "../product-service.service";

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})
export class ProductListComponent {
  value: string | undefined;
  products: Product[] = [];
  selectedFilter : string = 'None';
  filteredItems = [...products];
  share() {
    window.alert('The product has been shared!');
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
  filterByCategory() {
    if(this.selectedFilter == 'None') {
      this.filteredItems = [...products];
    }
    else {
      this.filteredItems = [...products].filter(p => p.category === this.selectedFilter);
    }
  }

  FilteredItem (event : any) {
    this.selectedFilter = event.target.value;
    this.filterByCategory();
  }

  incrementLikes(id : number) {
    products.filter(p => p.id === id).map(p => p.likes += 1)
  }

  deleteProduct(id : number) {
    this.products = this.products.filter(p => p.id !== id);
    this.filterByCategory();
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
