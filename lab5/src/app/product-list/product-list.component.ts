

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
  product = [...products];
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
      this.filteredItems = this.product;
    }
    else {
      this.filteredItems = this.product.filter(p => p.category === this.selectedFilter);
    }
  }

  FilteredItem (event : any) {
    this.selectedFilter = event.target.value;
    this.filterByCategory();
  }

  deleteProduct(id : number) {
    this.product = this.product.filter(p => p.id !== id);
    this.filterByCategory();
  }
}
