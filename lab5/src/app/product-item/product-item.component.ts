import {Component, Input, OnInit} from '@angular/core';
import {Product, products} from '../products';

@Component({
  selector: 'app-product-items',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  products = [...products];
  @Input() product: Product | undefined;
  selectedFilter : string = 'None';
  filteredItems = [...products];




  ngOnInit(): void {
  }

  filterByCategory() {
    if(this.selectedFilter == 'None') {
      this.filteredItems = this.products;
    }
    else {
      this.filteredItems = this.products.filter(p => p.category === this.selectedFilter);
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
    this.products = [...products].filter(p => p.id !== id);
    this.filterByCategory();
  }
}
