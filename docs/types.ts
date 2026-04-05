// types.ts

import { v4 as uuidv4 } from 'uuid';

type Id = string;
type Name = string;
type Description = string;
type Category = string;
type Location = string;
type Status = 'active' | 'inactive';

interface Product {
  id: Id;
  name: Name;
  description: Description;
  category: Category;
  location: Location;
  status: Status;
}

interface ProductResponse {
  id: Id;
  name: Name;
  description: Description;
  category: Category;
  location: Location;
  status: Status;
  createdAt: Date;
  updatedAt: Date;
}

interface ProductRequest {
  id?: string;
  name: Name;
  description: Description;
  category: Category;
  location: Location;
  status: Status;
}

interface Error {
  code: number;
  message: string;
}

interface Success<T> {
  data: T;
  message: string;
}

interface PagedResponse<T> {
  data: T[];
  page: number;
  per_page: number;
  total: number;
}

interface NewProduct {
  id: Id;
  name: Name;
  description: Description;
  category: Category;
  location: Location;
  status: Status;
}