"""
Figma Asset Sync
Automatically download assets from Figma and organize into project structure.
"""

import os
import sys
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FIGMA_TOKEN = os.getenv('FIGMA_ACCESS_TOKEN')
FIGMA_FILE_KEY = os.getenv('FIGMA_FILE_KEY')

if not FIGMA_TOKEN:
    print("ERROR: FIGMA_ACCESS_TOKEN not found in .env")
    sys.exit(1)

if not FIGMA_FILE_KEY:
    print("ERROR: FIGMA_FILE_KEY not found in .env")
    sys.exit(1)


class FigmaSync:
    """Sync assets from Figma to local project structure"""

    def __init__(self):
        self.token = FIGMA_TOKEN
        self.file_key = FIGMA_FILE_KEY
        self.base_url = "https://api.figma.com/v1"
        self.headers = {
            "X-Figma-Token": self.token
        }
        self.assets_dir = Path(__file__).parent.parent / "assets"

    def get_file_info(self):
        """Get file information and structure"""
        url = f"{self.base_url}/files/{self.file_key}"

        print(f"Connecting to Figma file: {self.file_key}...")
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            print(f"\nFile: {data['name']}")
            print(f"Last modified: {data.get('lastModified', 'Unknown')}")
            return data
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None

    def list_pages_and_frames(self, file_data):
        """List all pages and frames in the file"""
        if not file_data:
            return []

        structure = []
        document = file_data.get('document', {})

        for page in document.get('children', []):
            page_info = {
                'name': page.get('name'),
                'id': page.get('id'),
                'frames': []
            }

            for frame in page.get('children', []):
                frame_info = {
                    'name': frame.get('name'),
                    'id': frame.get('id'),
                    'type': frame.get('type')
                }
                page_info['frames'].append(frame_info)

            structure.append(page_info)

        return structure

    def get_exportable_images(self):
        """Get all images marked for export in the file"""
        url = f"{self.base_url}/files/{self.file_key}/images"

        print("\nFetching exportable images...")
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return data.get('meta', {}).get('images', {})
        else:
            print(f"Error fetching images: {response.status_code}")
            return {}

    def export_nodes(self, node_ids, format='png', scale=2):
        """
        Export specific nodes as images

        Args:
            node_ids: List of node IDs to export
            format: Image format (png, jpg, svg, pdf)
            scale: Export scale (1, 2, 3, 4)
        """
        if not node_ids:
            print("No node IDs provided for export")
            return {}

        # Figma API accepts comma-separated IDs
        ids_param = ','.join(node_ids)

        url = f"{self.base_url}/images/{self.file_key}"
        params = {
            'ids': ids_param,
            'format': format,
            'scale': scale
        }

        print(f"\nExporting {len(node_ids)} nodes as {format} (scale {scale}x)...")
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return data.get('images', {})
        else:
            print(f"Error exporting nodes: {response.status_code}")
            print(response.text)
            return {}

    def download_image(self, url, output_path):
        """Download an image from URL"""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'wb') as f:
                f.write(response.content)

            return True
        except Exception as e:
            print(f"Error downloading {output_path.name}: {e}")
            return False

    def organize_assets(self, file_data):
        """
        Analyze file structure and suggest organization into project folders
        """
        print("\n" + "="*60)
        print("FIGMA FILE STRUCTURE")
        print("="*60)

        structure = self.list_pages_and_frames(file_data)

        organization = {
            'logos': [],
            'team': [],
            'illustrations': [],
            'icons': [],
            'other': []
        }

        for page in structure:
            print(f"\nPage: {page['name']}")
            print(f"  ID: {page['id']}")
            print(f"  Frames: {len(page['frames'])}")

            # Categorize based on page/frame names
            page_name_lower = page['name'].lower()

            for frame in page['frames']:
                frame_name_lower = frame['name'].lower()

                try:
                    print(f"    - {frame['name']} ({frame['type']}) [ID: {frame['id']}]")
                except UnicodeEncodeError:
                    # Handle Unicode characters that can't be displayed in Windows console
                    safe_name = frame['name'].encode('ascii', 'ignore').decode('ascii')
                    print(f"    - {safe_name} ({frame['type']}) [ID: {frame['id']}]")

                # Categorize
                if 'logo' in page_name_lower or 'logo' in frame_name_lower:
                    organization['logos'].append({
                        'name': frame['name'],
                        'id': frame['id'],
                        'page': page['name']
                    })
                elif 'team' in page_name_lower or 'headshot' in frame_name_lower or 'photo' in frame_name_lower:
                    organization['team'].append({
                        'name': frame['name'],
                        'id': frame['id'],
                        'page': page['name']
                    })
                elif 'icon' in page_name_lower or 'icon' in frame_name_lower:
                    organization['icons'].append({
                        'name': frame['name'],
                        'id': frame['id'],
                        'page': page['name']
                    })
                elif 'illustration' in page_name_lower or 'graphic' in frame_name_lower:
                    organization['illustrations'].append({
                        'name': frame['name'],
                        'id': frame['id'],
                        'page': page['name']
                    })
                else:
                    organization['other'].append({
                        'name': frame['name'],
                        'id': frame['id'],
                        'page': page['name']
                    })

        return organization

    def download_all_assets(self, organization):
        """Download all categorized assets to appropriate folders"""
        print("\n" + "="*60)
        print("DOWNLOADING ASSETS")
        print("="*60)

        downloads = []

        # Download logos
        if organization['logos']:
            print(f"\nDownloading {len(organization['logos'])} logos...")
            node_ids = [item['id'] for item in organization['logos']]
            image_urls = self.export_nodes(node_ids, format='png', scale=2)

            for item in organization['logos']:
                if item['id'] in image_urls:
                    filename = item['name'].lower().replace(' ', '-') + '.png'
                    output_path = self.assets_dir / 'brand' / 'logos' / filename
                    if self.download_image(image_urls[item['id']], output_path):
                        downloads.append(str(output_path))
                        print(f"  [OK] {filename}")

        # Download team photos
        if organization['team']:
            print(f"\nDownloading {len(organization['team'])} team photos...")
            node_ids = [item['id'] for item in organization['team']]
            image_urls = self.export_nodes(node_ids, format='png', scale=2)

            for item in organization['team']:
                if item['id'] in image_urls:
                    filename = item['name'].lower().replace(' ', '-') + '.png'
                    output_path = self.assets_dir / 'team' / 'headshots' / filename
                    if self.download_image(image_urls[item['id']], output_path):
                        downloads.append(str(output_path))
                        print(f"  [OK] {filename}")

        # Download illustrations
        if organization['illustrations']:
            print(f"\nDownloading {len(organization['illustrations'])} illustrations...")
            node_ids = [item['id'] for item in organization['illustrations']]
            image_urls = self.export_nodes(node_ids, format='png', scale=2)

            for item in organization['illustrations']:
                if item['id'] in image_urls:
                    filename = item['name'].lower().replace(' ', '-') + '.png'
                    output_path = self.assets_dir / 'illustrations' / 'concepts' / filename
                    if self.download_image(image_urls[item['id']], output_path):
                        downloads.append(str(output_path))
                        print(f"  [OK] {filename}")

        # Download icons
        if organization['icons']:
            print(f"\nDownloading {len(organization['icons'])} icons...")
            node_ids = [item['id'] for item in organization['icons']]
            image_urls = self.export_nodes(node_ids, format='png', scale=2)

            for item in organization['icons']:
                if item['id'] in image_urls:
                    filename = item['name'].lower().replace(' ', '-') + '.png'
                    output_path = self.assets_dir / 'illustrations' / 'icons' / filename
                    if self.download_image(image_urls[item['id']], output_path):
                        downloads.append(str(output_path))
                        print(f"  [OK] {filename}")

        # Download other assets
        if organization['other']:
            print(f"\nDownloading {len(organization['other'])} other assets...")
            node_ids = [item['id'] for item in organization['other']]
            image_urls = self.export_nodes(node_ids, format='png', scale=2)

            for item in organization['other']:
                if item['id'] in image_urls:
                    filename = item['name'].lower().replace(' ', '-') + '.png'
                    output_path = self.assets_dir / 'illustrations' / 'concepts' / filename
                    if self.download_image(image_urls[item['id']], output_path):
                        downloads.append(str(output_path))
                        print(f"  [OK] {filename}")

        return downloads

    def sync(self):
        """Main sync function"""
        print("="*60)
        print("FIGMA ASSET SYNC")
        print("="*60)

        # Get file info
        file_data = self.get_file_info()
        if not file_data:
            print("\nFailed to connect to Figma. Check your token and file key.")
            return False

        # Analyze structure
        organization = self.organize_assets(file_data)

        # Summary
        print("\n" + "="*60)
        print("ASSET SUMMARY")
        print("="*60)
        print(f"Logos: {len(organization['logos'])}")
        print(f"Team Photos: {len(organization['team'])}")
        print(f"Illustrations: {len(organization['illustrations'])}")
        print(f"Icons: {len(organization['icons'])}")
        print(f"Other: {len(organization['other'])}")
        print(f"Total: {sum(len(v) for v in organization.values())}")

        # Ask for confirmation
        print("\n" + "="*60)
        response = input("\nDownload all assets? (y/n): ")

        if response.lower() == 'y':
            downloads = self.download_all_assets(organization)

            print("\n" + "="*60)
            print("SYNC COMPLETE")
            print("="*60)
            print(f"Downloaded {len(downloads)} assets")
            print(f"\nAssets saved to: {self.assets_dir}")

            # Save manifest
            manifest_path = self.assets_dir / 'figma-sync-manifest.json'
            with open(manifest_path, 'w') as f:
                json.dump({
                    'file_key': self.file_key,
                    'file_name': file_data['name'],
                    'sync_date': file_data.get('lastModified'),
                    'organization': organization,
                    'downloaded': downloads
                }, f, indent=2)

            print(f"Manifest saved to: {manifest_path}")
            return True
        else:
            print("\nSync cancelled.")
            return False


def main():
    syncer = FigmaSync()
    syncer.sync()


if __name__ == "__main__":
    main()
